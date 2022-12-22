   
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [ 
    path('signup/', views.signup ),
    path('login/', views.login_page ),
    path('profile/', views.profile ),
    path('logout/', views.logout_page ),
]
