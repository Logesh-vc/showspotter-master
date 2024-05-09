from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request) :
    return render(request,"login/backend-html")

def user_login(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username =='admin' and password=='admin':
            return HttpResponseRedirect(reverse('dashboard:theatre-manager-view'))
        else :
            return HttpResponse("Login Failed")

    else :
        return render(request,'login/backend-login.html')


