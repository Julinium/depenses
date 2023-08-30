from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        context = {'message':'You are known, we know you, ...'}
        return render(request, 'base/home.html', context)        
    else:
        context = {'message':'Who the hell are you in this world ? ...'}
        return render(request, 'base/home.html', context)