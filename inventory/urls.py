from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),
]
