from django.shortcuts import render,redirect
from adminSite.views import dashboard
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return render(request,'login.html')



    