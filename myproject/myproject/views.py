from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'index.html', {})

def logout_view(request):
    logout(request)
    return redirect('index')

def login_view(request):
    error_message = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('index')

            else:
                error_message = 'Ups.Something went wrong...'
    
    context = {
        'form': form, 
        'error_message': error_message
        }
    return render(request, 'login.html', context=context)
    