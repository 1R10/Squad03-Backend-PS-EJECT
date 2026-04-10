from django.urls import path
from . import views

urlpatterns = [
    path('',          views.index,    name= 'homepage'), # '' vazio para cair DIRETO da home ~Ryan
    path('blog/',     views.blog,     name= 'blog'),
    path('about/',    views.about,    name= 'about.html'),
    path('reservar/', views.reservar, name='reservar'),


]