from django.contrib import admin
from django.urls import path
from . import views  
from . import addFav
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     
    
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
     path('addToFav/', addFav.addToFav, name='addToFav'),
     path('uploader/', views.ProfileEditor, name='ProfileEditor'),
     path('ProfileData/', views.ProfileData, name='ProfileData'),

      
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)