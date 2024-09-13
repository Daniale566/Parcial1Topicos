from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_flight, name='register_flight'),
    path('list/', views.list_flights, name='list_flights'),
    path('statistics/', views.flight_statistics, name='flight_statistics'),
]