from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'message':'This message was passed from the View...'}
    return render(request, 'base/home.html', context)