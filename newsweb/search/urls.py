 
from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
     
    path('search/', views.search, name='search'),
    path('save/', views.save_data, name='save'),
   
]
