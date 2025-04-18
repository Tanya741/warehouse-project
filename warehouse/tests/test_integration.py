import os
from django.test import TestCase, RequestFactory, Client
from warehouse.models import Product, Category
from warehouse.views import(
    product_list, product_detail, product_new, product_edit, product_delete, product_fetch, product_category, category_new, category_detail, category_edit, category_delete, category_fetch

)
from django.urls import reverse
from django.http import HttpRequest
from django.conf import settings
import mongoengine
import unittest
from seeds.seed import run_seed_data

# if not settings.configured:
#     settings.configure(
#         DATABASES={
#             'default': {
#                 'ENGINE': 'django.db.backends.dummy'
#             }
#         }
#     )
#     django.setup()
class Integrationtest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       run_seed_data()
    

    def setUp(self):
        # mongoengine.connect(db="New", host="mongodb://localhost:27017/")
        self.client = Client()
        self.sample_product = Product.objects.first()
        self.sample_category = Category.objects.first()

    def tearDown(cls):
        Product.drop_collection()
        Category.drop_collection()
        run_seed_data()

    @classmethod
    def tearDownClass(cls):
        Product.drop_collection()
        Category.drop_collection()
    

    def test_product_list(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        response = self.client.get(reverse('product_detail', args = [str(self.sample_product.pk)]))
        self.assertEqual(response.status_code, 200)

    def test_product_new(self):
        data = {
            'name': 'New product',
            'description': 'Test Desc',
            'category': str(self.sample_category.pk),
            'price': 100,
            'brand': 'BrandX',
            'quantity': 5
        }
        response = self.client.post(reverse('product_new'), data)
        self.assertEqual(response.status_code, 302)

    def test_product_edit(self):
        data ={
            'name': 'Edited Product',
            'description': 'Updated desc',
            'category': str(self.sample_product.category),
            'price': 200,
            'brand': 'BrandY',
            'quantity': 10
        }
        response = self.client.post(reverse('product_edit', args =[str(self.sample_product.pk)]), data)
        self.assertEqual(response.status_code, 302)

    def test_product_delete(self):
        response = self.client.post(reverse('product_delete', args=[str(self.sample_product.pk)]))
        self.assertEqual(response.status_code, 302)

    def test_product_fetch(self):
        response = self.client.get(reverse('product_fetch', args=[self.sample_product.name]))
        self.assertEqual(response.status_code, 200)

    def test_product_category(self):
        response = self.client.get(reverse('product_category'))
        self.assertEqual(response.status_code, 200)

    def test_category_new(self):
        data = {
            'title': 'New Category',
            'description': 'Category Desc'
        }
        response = self.client.post(reverse('category_new'), data)
        self.assertEqual(response.status_code, 302)

    def test_category_detail(self):
        response = self.client.get(reverse('category_detail', args=[str(self.sample_category.pk)]))
        self.assertEqual(response.status_code, 200)

    def test_category_edit(self):
        data = {
            'title': 'Edited Category',
            'description': 'Updated Desc'
        }
        response = self.client.post(reverse('category_edit', args=[str(self.sample_category.pk)]), data)
        self.assertEqual(response.status_code, 302)

    def test_category_delete(self):
        response = self.client.post(reverse('category_delete', args=[str(self.sample_category.pk)]))
        self.assertEqual(response.status_code, 302)

    def test_category_fetch(self):
        response = self.client.get(reverse('category_fetch', args=[str(self.sample_category.pk)]))
        self.assertEqual(response.status_code, 200)

    def test_product_new_cat(self):
        data = {
            'name': 'Product in Cat',
            'description': 'Desc',
            'price': 50,
            'brand': 'TestBrand',
            'quantity': 3
        }
        response = self.client.post(reverse('product_new_cat', args=[str(self.sample_category.pk), str(self.sample_category.pk)]), data)
        self.assertEqual(response.status_code, 200)

    

