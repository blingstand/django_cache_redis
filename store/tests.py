from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse
from .models import Product

# Create your tests here.
def create_one_entry():
    p = Product(name='product_name')
    p.save()

class TestViews(TestCase): 

    def setUp(self):
        create_one_entry()

    def tearDown(self):
        cache.clear()

    def test_view_books(self): 
        """ send a get request to http://test_server/store/"""
        response = self.client.get(reverse('store:database'))
        
        #need to avoid issue with time
        id, name = response.json()[0]['id'], response.json()[0]['name']
        self.assertEqual(id, 1)
        self.assertEqual(name, 'product_name')

    def test_view_cached_books(self):
        """ send a get request to http://test_server/store/cache""" 
        self.assertEqual(cache.get('product'), None)
        response = self.client.get(reverse('store:cache'))
        id, name = response.json()[0]['id'], response.json()[0]['name']
        #same result but cache is different
        self.assertEqual(id, 1)
        self.assertEqual(name, 'product_name')
        self.assertTrue(cache.get('product') != None)