from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from clothsite import settings
from mikhalchuk.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mikhalchuk.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
