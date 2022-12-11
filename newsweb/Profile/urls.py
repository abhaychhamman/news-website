from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
     
    
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('UserProfile/', views.UserProfile, name='UserProfile'),
   
]
