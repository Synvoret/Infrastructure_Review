from django import forms
from .models import Tour


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'


class Transformers(forms.Form):
    tr11 = forms.BooleanField(required=False)
    tr12 = forms.BooleanField(required=False)
    tr21 = forms.BooleanField(required=False)
    tr31 = forms.BooleanField(required=False)
    tr41 = forms.BooleanField(required=False)
    tr42 = forms.BooleanField(required=False)
    temp_A1 = forms.BooleanField(required=False, initial=True)
    temp_A2 = forms.BooleanField(required=False, initial=True)
    temp_A3 = forms.BooleanField(required=False, initial=True)
    temp_rdzen = forms.BooleanField(required=False)
    select_all = forms.BooleanField(required=False)


class UPSy(forms.Form):
    ups_1_34 = forms.BooleanField(required=False)
    ups_tt = forms.BooleanField(required=False)
    ups_GPD = forms.BooleanField(required=False)
    ups_BL04BM = forms.BooleanField(required=False)
    ups_BL06ID = forms.BooleanField(required=False)
    ups_BL04ID = forms.BooleanField(required=False)
    ups_BL10BM = forms.BooleanField(required=False)
    ups_BL09BM = forms.BooleanField(required=False)
    ups_BL05ID = forms.BooleanField(required=False)
    ups_PPOZ = forms.BooleanField(required=False)
    working_temp = forms.BooleanField(required=False)
    l1 = forms.BooleanField(required=False)
    l2 = forms.BooleanField(required=False)
    l3 = forms.BooleanField(required=False)
    load = forms.BooleanField(required=False)


class Capacitors_Battery(forms.Form):
    bat11 = forms.BooleanField(required=False)
    bat12 = forms.BooleanField(required=False)
    bat21 = forms.BooleanField(required=False)
    bat31 = forms.BooleanField(required=False)
    temp = forms.BooleanField(required=False)
    weekly_TPF = forms.BooleanField(required=False)


class RGEAC(forms.Form):
    rozdz_rge_ac = forms.BooleanField(required=False, initial=True)
    supply_tor_1 = forms.BooleanField(required=False)
    supply_tor_2 = forms.BooleanField(required=False)