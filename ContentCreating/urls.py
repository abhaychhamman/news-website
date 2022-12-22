 
from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
     
    
    path('ContentPage/', views.ContentPage, name='ContentPage'),
    path('Channel/<str:user>/', views.UserChannel, name='Channel'),
    path('EditChannel/', views.EditChannel, name='EditChannel'),
    path('ChannelData/', views.ChannelData, name='ChannelData'),
    path('create/<str:channelType>', views.ContentCreation, name='ContentCreation'),
   
]
