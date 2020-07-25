from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('sales/', views.login_view, name='list_sales'),
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),

]
