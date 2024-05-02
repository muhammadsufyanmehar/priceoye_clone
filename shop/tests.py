# shop/tests.py

from django.test import TestCase
from brands.models import Brand
from categories.models import Category
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')

    def test_product_creation(self):
        product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            price=100.0,
            stock_quantity=50,
            brand=self.brand,
            category=self.category
        )
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'This is a test product')
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.stock_quantity, 50)
        self.assertEqual(product.brand, self.brand)
        self.assertEqual(product.category, self.category)
