from django.shortcuts import render
from . models import Expense

def home(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.all()
        message = "You are known, we know you, ..."
        context = {'message': message,
                   'expenses': expenses}
        return render(request, 'base/home.html', context)        
    else:
        context = {'message':'Welcome. This is a great app. Login to use it.'}
        return render(request, 'base/welcome.html', context)