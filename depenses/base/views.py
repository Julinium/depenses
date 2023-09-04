from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from base.models import Expense, Income, Transfer, Account
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
    incomes = Income.objects.all().filter(account__user=request.user)
    expenses = Expense.objects.all().filter(account__user=request.user)
    transfers = Transfer.objects.all().filter(fm__user=request.user).filter(to__user=request.user)
    xtotal = 0
    for e in expenses: xtotal += e.amount
    ntotal = 0
    for i in incomes: ntotal += i.amount
    perfo = ntotal - xtotal
    context = {'incomes': incomes,
               'transfers': transfers,
               'expenses': expenses,
               'ntotal': ntotal,
               'xtotal': xtotal,
               'perfo': perfo}
    return render(request, 'base/home.html', context)


@login_required(login_url="login")
def accounts_list(request):
    accounts = Account.objects.all().filter(user=request.user)
    context = {'accounts': accounts}
    return render(request, 'base/accounts.html', context)
    
    
    
def wip(request):
    context = {'message':_("The requested ressource is being made at this time.")}
    return render(request, 'base/wip.html', context)