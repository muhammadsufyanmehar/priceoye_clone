# orders/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Order, OrderDetail, Cart
from shop.models import Product
# Create your tests here.
class OrderModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',  # Provide a username here
            email='testuser@example.com', # Provide an email address here
            password='testpassword' # Provide a password here
        )
# Create a product
    def test_order_creation(self):
        order = Order.objects.create(user=self.user, total_amount=100.0)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.total_amount, 100.0)
# Create your tests here.
class OrderDetailModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',  # Provide a username here
            email='testuser@example.com',
            password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='Product Description',
            price=50.0,
            stock_quantity=10
        )
        self.order = Order.objects.create(user=self.user, total_amount=100.0)

    def test_order_detail_creation(self): # Create an order detail
        order_detail = OrderDetail.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            subtotal=100.0
        )
        self.assertEqual(OrderDetail.objects.count(), 1)
        self.assertEqual(order_detail.order, self.order)
        self.assertEqual(order_detail.product, self.product)
        self.assertEqual(order_detail.quantity, 2)
        self.assertEqual(order_detail.subtotal, 100.0)

class CartModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',  # Provide a username here
            email='testuser@example.com',
            password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='Product Description',
            price=50.0,
            stock_quantity=10
        )

    def test_cart_creation(self): # Create a cart
        cart = Cart.objects.create(user=self.user, product=self.product, quantity=3)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(cart.user, self.user)
        self.assertEqual(cart.product, self.product)
        self.assertEqual(cart.quantity, 3)
