from django.urls import path
from . import views

urlpatterns = [
    path('',                      views.index,                name= 'homepage'),             # '' vazio para cair DIRETO da home ~Ryan
    path('blog/',                 views.blog,                 name= 'blog'),
    path('about/',                views.about,                name= 'about'),
    path('reservar/',             views.reservar,             name= 'reservar'),             # redireciona pra essa pag fantasma q puxa o forms, mas RE-redireciona pra página atual por causa do redirect ~Ryan
    path('reservar_restaurante/', views.reservar_restaurante, name= 'reservar_restaurante')


]