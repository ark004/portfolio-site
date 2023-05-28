from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import RegistrationForm
from face import views

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:user_login')
    else:
        return redirect('account:user_login')

        form = RegistrationForm()
    return render(request, 'account/reg.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('face:my_view')
        else:
            return redirect('face:my_view')
    return render(request, 'account/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')
