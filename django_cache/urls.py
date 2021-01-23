# django_cache/urls.py
 

from django.urls import path, include
from django.contrib import admin
APP_NAME = 'django_cache'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include(('store.urls', 'store'), namespace='store'))
]