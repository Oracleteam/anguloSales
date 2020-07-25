from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect("list_sales", request)
        else:
            template = loader.get_template('inventory/login.html')
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('inventory/login.html')
        return HttpResponse(template.render(context, request))



@login_required
def list_sales(request):
    """ show list of sales """
    context = {}
    template = loader.get_template('inventory/sales_list.html')
    return HttpResponse(template.render(context, request))


def _logout(request):
    """ logaut inner function """
    context = {}
    logout(request)
    template = loader.get_template('inventory/login.html')
    return HttpResponse(template.render(context, request))


def _isRec(request):
    """ is loged in inner function """
    context = {}
    if not request.user.is_authenticated:
        template = loader.get_template('inventory/login.html')
        return HttpResponse(template.render(context, request))

