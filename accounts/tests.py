from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserModelTest(TestCase):
    def test_custom_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            first_name='Test',
            last_name='User',
            password='testpassword',
        )

        # Check if the user is created successfully
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertTrue(user.check_password('testpassword'))

    def test_custom_user_email_field(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            first_name='Test',
            last_name='User',
            password='testpassword',
        )

        # Check if the email field is set correctly
        self.assertEqual(user.email, 'test@example.com')
