from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from base.models import Expense, Income, Transfer, Account, AccountBalance
from django.contrib.auth.decorators import login_required
# from django.shortcuts import  render, redirect
from .forms import NewUserForm, AccountForm
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
            return redirect("login")
        messages.error(request, _("Unsuccessful registration. Invalid information."))
    else:
        form = NewUserForm()
    context={"register_form": form}
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


@login_required(login_url="login")
def expenses(request):
    expenses = Expense.objects.all().filter(account__user=request.user)
    context = {"expenses":expenses}
    return render(request, 'base/expenses.html', context)


@login_required(login_url="login")
def expense(request, pk):
    expense = Expense.objects.get(id=pk)
    print(expense.account.user)
    print(request.user)
    if expense.account.user == request.user:
        context = {"expense":expense, "pk": pk}
        return render(request, 'base/expense.html', context)
    
    context = {
        'title': _("Non authorized"),
        'message': _("You are not authorized to acces the requested ressource.")}
    return render(request, 'base/wip.html', context)


@login_required(login_url="login")
def account_form(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            if account.save():
                messages.success(request, _("Account created successfully."))
                accoubal = AccountBalance.objects.create(balance=account.balance)
                # accoubal.balance = account.balance
                accoubal.save()
                print(accoubal)
            else:
                messages.error(request, _("Account saving error. Invalid information."))
        return redirect("accounts")
        messages.error(request, _("Account creation error. Invalid information."))
    else:
        form = AccountForm()
    context={"form": form}
    return render (request, "base/account_form.html", context)


def wip(request):
    title = _("It's not you...")
    message = _("The requested ressource is not (yet) available.")
    context = {
        'title': title,
        'message': message}
    return render(request, 'base/wip.html', context)