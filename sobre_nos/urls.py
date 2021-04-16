from django.urls import path

from . import views

urlpatterns = [
    path('', views.sobre_nos, name='sobre_nos_home'),
]