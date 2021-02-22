from django.shortcuts import render,redirect
from adminSite.views import dashboard
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return render(request,'base.html')
    else:
        return render(request,'login.html')


def home2(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return render(request,'login.html') 
    