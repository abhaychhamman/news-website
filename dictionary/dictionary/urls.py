   
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dict.urls')),
    path('', include('Profile.urls')),
    path('', include('Test.urls')),
    path('', include('Translate.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)