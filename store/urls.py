from django.urls import path
from .views import view_books, view_cached_books
 
APP_NAME = 'store'

urlpatterns = [
    path('', view_books, name="database"),
    path('cache/', view_cached_books, name="cache")
]