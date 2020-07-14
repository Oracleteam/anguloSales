from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.index, name='login'),
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),
]
