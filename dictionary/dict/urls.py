 
import django


from django.contrib import admin
from django.urls import path

from dict.models import Dictionary
from .  import views


urlpatterns = [
    path("dict",views.dictionary,name="dictionary"),
    path("show_dict",views.show_dict,name="show_dict"),
    path("",views.index,name="show_dict"),
    path("save",views.save_data,name="save"),
    path("saveFavourite",views.saveFav,name="saveFavourite"),
    path("contact",views.contactUs,name="contact"),
    path("about",views.about,name="about"),
    path("",views.index,name="index"),
]
