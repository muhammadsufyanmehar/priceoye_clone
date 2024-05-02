from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):
    def setUp(self):
        # Create a sample category for testing
        Category.objects.create(name='Test Category')

    def test_category_name(self):
        """Test the name field of the Category model."""
        category = Category.objects.get(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

    def test_category_str_method(self):
        """Test the __str__ method of the Category model."""
        category = Category.objects.get(name='Test Category')
        self.assertEqual(str(category), 'Test Category')
