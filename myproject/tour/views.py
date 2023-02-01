import re
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TourForm, Transformers, UPSy, Capacitors_Battery, RGEAC
from .models import Tour
from .utils import get_plot
from datetime import datetime
import pandas as pd
from typing import Pattern

def index(request):
    message = None
    context = {'message': message}
    return render(request, 'tour/index.html', context=context)


class NewTour(View):

    date = datetime.now().strftime('%d-%m-%Y')
    message = None

    def get(self, request):        
        context = {
            'form': TourForm(),
            'date': self.date,
            'message': self.message
        }
        return render(request, 'tour/new_tour.html', context=context)

    def post(self, request):
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': TourForm(),
                'message': "Obchód zapisany poprawnie."
            }
            return render(request, 'tour/new_tour.html', context=context)
        else:
            context = {
                'form': TourForm(),
                'message_bad': "Wystąpił błąd zapisu obchodu."
            }
            return render(request, 'tour/new_tour.html', context=context)


class Charts(View):
    
    def get(self, request, type_chart):
        context = {
            'transformers_form': Transformers(),
            'upsy_form': UPSy(),
            'cap_bat_form': Capacitors_Battery(),
            'rge_ac_form': RGEAC(),
            "type_chart": type_chart
        }
        return render(request, 'tour/charts.html', context=context)

    def post(self, request, type_chart):
        context = {}
        message = None
        
        # TRANSFORMATORY
        if 'button-submit-transformers' in request.POST:
            transformers_form = Transformers(request.POST)            
            devices, parameters = self.get_devices_and_parameters(transformers_form, r"tr\d{2}", [r"temp_."])            
            title = "Wykres temperaturowy Transformatorów"
            legend_device = [f"Trafo TR{device[-2:-1]}.{device[-1:]}" for device in devices]
            legend_parameter = [f"Czujnik {parameter[-2:]}" for parameter in parameters]
            legends = [f"{dev}, {par}" for dev in legend_device for par in legend_parameter]
            ylabel = "Temperatura [℃]"
            context['transformers_form'] = transformers_form

        # UPSy
        if 'button-submit-upsy' in request.POST:
            upsy_form = UPSy(request.POST)
            devices, parameters = self.get_devices_and_parameters(upsy_form, r"ups_.", [r"working_temp", r"l\d", r"load"]) 
            if 'load' in parameters and any(l in parameters for l in ['l1', 'l2', 'l3']):
                message = "Źle wybrane parametry"
            elif 'load' in parameters and any(d in devices for d in ["ups_1_34", "ups_tt", "ups_GPD", "ups_BL04BM", "ups_BL06ID", "ups_BL04ID", "ups_BL10BM", "ups_BL09BM"]):
                message = "Źle dobrane parametry. UPS 3faz. do obciążenia Omegi."
            elif any(l in parameters for l in ['l1', 'l2', 'l3']) and any(d in devices for d in ["ups_BL05ID", "ups_PPOZ"]):
                message = "Źle dobrane parametry. Omega do obciążenia 3faz."
            else:
                if 'working_temp' in parameters:                    
                    title = "Wykres temperaturowy UPSów"
                    legends = [f"UPS {device[4:]}" for device in devices]
                    ylabel = "Temperatura [℃]"          
                elif 'load' in parameters:                    
                    title = "Wykres obciążenia UPSów Omega"            
                    legends = [f"UPS {device[4:]}" for device in devices]
                    ylabel = 'Obciążenie [VA]'
                elif 'l1' or 'l2' or 'l3' in parameters:                    
                    title = "Wykres obciążenia UPSów"            
                    legend_dev = [f"UPS {device[4:]}" for device in devices]
                    legend_par = ["Faza {}".format(parameter.capitalize()) for parameter in parameters]
                    legends = [f"{i}, {j}" for i in legend_dev for j in legend_par]
                    ylabel = 'Obciążenie [%]'
            context['upsy_form'] = upsy_form
        
        # BATERIE KONDENSATORÓW
        if 'button-submit-cap-battery' in request.POST:
            legends = None
            cap_bat_form = Capacitors_Battery(request.POST)
            devices, parameters = self.get_devices_and_parameters(cap_bat_form, r"bat\d{2}", [r"temp", r"weekly_TPF"])
            if 'temp' in parameters:
                title = "Wykres temperaturowy Baterii Kondensatorów"
                legends = [f"Bateria RG{device[-2:-1]}.{device[-1:]}" for device in devices]
                ylabel = "Temperatura [℃]"
            elif 'weekly_TPF' in parameters:
                title = "Wykres TPF baterii kondensatorów"            
                legend_dev = [f"Bateria RG{device[-2:-1]}.{device[-1:]}" for device in devices]
                legend_par = [f"{parameter[:6].capitalize()}{parameter[6:].upper()}" for parameter in parameters]
                legends = [f"{i}, {j}" for i in legend_dev for j in legend_par]
                ylabel = 'Tygodniowe TPF'
            context['cap_bat_form'] = cap_bat_form

        # RGE-A,C        
        if 'button-submit-rge-ac' in request.POST:
            rge_ac_form = RGEAC(request.POST)
            devices, parameters = self.get_devices_and_parameters(rge_ac_form, r"rozdz_rge_ac", [r"supply_tor_\d{1}"]) 
            title = "Rozdzielnica RGE-A,C - zasilanie"
            legends = [f"Zasilanie - tor {number[-1:]}" for number in parameters]
            ylabel = "Napięcie [V]"
            context['rge_ac_form'] = rge_ac_form
        
        try:
            context.update(
                {
                'chart': self.charts(ydata=self.char_values(devices, parameters), title=title, legends=legends, ylabel=ylabel)
                }
            )
        except:
            pass
        finally:
            context.update(
                {
                "type_chart": type_chart,
                "message": message
                }
            )
            return render(request, 'tour/charts.html', context=context)
    
    def charts(self, **kwargs):
        '''Function generating chart.'''
        ydata = kwargs['ydata']
        title = kwargs['title']
        legends = kwargs['legends']
        ylabel = kwargs['ylabel']        
        chart = get_plot(df=ydata, title=title, legends=legends, ylabel=ylabel)
        return chart
    
    def get_devices_and_parameters(self, form, reg_device: Pattern, reg_parameter_list: list[Pattern]):
        '''Generator making two lists, for choosen devices and choosen parameters'''
        devices = [device for device in form.data if re.match(reg_device, device)]
        parameters = [parameter for parameter in form.data if any(re.match(reg, parameter) for reg in reg_parameter_list)]
        yield devices
        yield parameters
    
    def char_values(self, devices: list[str], parameters: list[str]):
        '''Function generating DataFrame from choosen option by user.'''
        columns = [f"{device}_{parameter}" for device in devices for parameter in parameters]        
        xdata = Tour.objects.values_list('date', flat=True)
        dates = [date.strftime('%Y-%m-%d') for date in xdata]
        data = Tour.objects.values(*columns)
        df = pd.DataFrame(data=data, index=dates)
        df = df.sort_index(ascending=True)
        return df


class History(ListView):
    template_name = "tour/history.html"
    paginate_by = 10
    model = Tour
    ordering = ["-date"]
    context_object_name = "tours"
    
    def get_queryset(self):
        start_date = self.request.GET.get('date-from')
        end_date = self.request.GET.get('date-to')
        queryset = super().get_queryset()
        if start_date and end_date:
            queryset = Tour.objects.filter(date__range=[start_date, end_date]).order_by('-date')
        return queryset


def edit_tour(request, id):
    tour = get_object_or_404(Tour, pk=id)
    form = TourForm(request.POST or None, instance=tour)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(to='tour:history')
        else:
            pass
    context = {
        'form': form
    }
    return render(request, 'tour/edit_tour.html', context=context)

def delete_tour(request, id):
    tour = get_object_or_404(Tour, pk=id)
    if request.method == 'POST':
        tour.delete()
        return redirect(to='tour:history')
    return render(request, 'tour/delete_tour.html', {'tour': tour})
