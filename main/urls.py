from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('masters/', views.masters, name='masters'),
    path('appointment/', views.appointment, name='appointment'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]