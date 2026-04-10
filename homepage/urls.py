from django.urls import path
from . import views

urlpatterns = [
    path('',          views.index,    name= 'homepage'), # '' vazio para cair DIRETO da home ~Ryan
    path('about/',    views.about,    name= 'about'),
    path('reservar/', views.reservar, name='reservar'),


]