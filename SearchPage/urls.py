from django.contrib import admin
from django.urls import path,include
from .views import search,save_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Search/', search,name="search"),
    path('save', save_data,name="save"),
   
 
    
]