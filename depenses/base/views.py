from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . models import Expense
from django.utils.translation import gettext_lazy as _


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a page after successful login
        else:
            # Handle invalid credentials
            pass
    return render(request, 'base/login.html')

def register_view(request):
    # Implement user registration logic here using Django forms or models
    return render(request, 'base/register.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to the login page after logout
    return render(request, 'base/logout.html')


def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def legal(request):
    context = {}
    return render(request, 'base/legal.html', context)


def home(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.all()
        message = _("You are known, we know you, ...")
        context = {'message': message,
                   'expenses': expenses}
        return render(request, 'base/home.html', context)        
    else:
        context = {'message':_("Welcome. This is a great app. Login to use it.")}
        return render(request, 'base/welcome.html', context)