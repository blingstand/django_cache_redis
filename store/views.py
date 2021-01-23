from django.shortcuts import render
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@api_view(['GET'])
def view_books(request):
    """this function search all products from db"""
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def view_cached_books(request):
    """this function search all products from db BUT 
    if the cache has a 'product' key, so get prod from cache
    else ask db and keep result in db
    """
    if 'product' in cache:
        # get results from cache
        products = cache.get('product')
        return Response(products, status=status.HTTP_201_CREATED)
 
    else:
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        # store data in cache
        cache.set('product', results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_201_CREATED)