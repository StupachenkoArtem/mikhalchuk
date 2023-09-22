from django.conf import settings
from django.urls import path, re_path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('collections/', collections, name='collections'),
    path('gallery/', gallery, name='gallery'),
    path("MIKHAL'CHUK/", mikhalchuk, name="MIKHAL'CHUK"),
    path('contact/', contact, name='contact'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('newcollection/', new_collection, name='new_collection'),
    path('jackets/', jackets, name='jackets'),
    path('dress/', dress, name='dress'),
    path('shirts_and_blouses/', shirts_and_blouses, name='shirts_and_blouses'),
    path('trousers_and_skirts/', trousers_and_skirts, name='trousers_and_skirts'),
    path('favicon.ico', favicon_ico, name='favicon.ico')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
