from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
     
    
    path('Trending News/', views.TrendingNews, name='TrendingNews')
]
