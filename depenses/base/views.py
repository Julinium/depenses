from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from base.models import Expense
from django.contrib.auth.decorators import login_required
# from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages


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
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _("Registration successful."))
            return redirect("home")
        messages.error(request, _("Unsuccessful registration. Invalid information."))
    else:
        form = NewUserForm()
    context={"register_form":form}
    return render (request, "base/register.html", context)


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


@login_required(login_url="login")
def home(request):
    
    expenses = Expense.objects.all().filter(account__user=request.user)
    message = _("You are known, we know you, ...")
    context = {'message': message,
               'expenses': expenses}
    return render(request, 'base/home.html', context)
    # if request.user.is_authenticated:
    # else:
    #     context = {'message':_("Welcome. This is a great app. Login to use it.")}
    #     return render(request, 'base/welcome.html', context)
    
    
def wip(request):
    context = {'message':_("The requested ressource is being made at this time.")}
    return render(request, 'base/wip.html', context)