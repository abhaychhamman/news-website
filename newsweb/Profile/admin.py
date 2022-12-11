from django.contrib import admin

from Profile.views import profile

from .models import Profile,UseProfile,Profile_info


# Register your models here.
admin.site.register(Profile)
admin.site.register(UseProfile)
admin.site.register(Profile_info)
