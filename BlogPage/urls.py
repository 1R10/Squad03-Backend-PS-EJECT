
from django.urls import path
from . import views

urlpatterns = [
    path('pages/', views.blog_page, name='blog_page'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),
]