from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
# auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# modelos
from inventory.models import *

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_sales')

        else:
            template = loader.get_template('inventory/login.html')
            return HttpResponse(template.render(context, request))
    else:
        logout(request)
        template = loader.get_template('inventory/login.html')
        return HttpResponse(template.render(context, request))


@login_required
def list_sales(request):
    """ show list of sales """
    context = {}
    template = loader.get_template('inventory/sales_list.html')
    return HttpResponse(template.render(context, request))


@login_required
def getSales(request):
    """ make json with sales """
    sl = sale.objects.select_related(sale_detail, client, product)
    sales_list = list(sl)  # important: convert the QuerySet to a list object
    return JsonResponse(sales_list, safe=False)