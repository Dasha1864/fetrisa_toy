from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu),
    path('toys/', views.toys),
    path('sets/', views.sets),
    path('stocks/', views.stocks),
    path('process/', views.process),
    path('ets/', views.ets),
]

