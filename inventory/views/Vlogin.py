from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            template = loader.get_template('inventory/index.html')
            return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('inventory/login.html')
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('inventory/login.html')
        return HttpResponse(template.render(context, request))