from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
     
    
    path('Memes/', views.Memes, name='TrendingNews')
]
