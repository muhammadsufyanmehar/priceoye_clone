from django.test import TestCase
from .models import Brand

class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Brand.objects.create(name='Test Brand')

    def test_name_max_length(self):
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_unique_name(self):
        brand = Brand(name='Test Brand')
        with self.assertRaises(Exception):
            brand.full_clean()
