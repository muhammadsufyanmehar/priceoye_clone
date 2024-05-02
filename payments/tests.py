# payments/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from orders.models import Order
from .models import Payment, Invoice

class PaymentModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_payment_creation(self):
        payment = Payment.objects.create(
            user=self.user,
            amount=50.0,
            success=True
        )
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(payment.user, self.user)
        self.assertEqual(payment.amount, 50.0)
        self.assertTrue(payment.success)

class InvoiceModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.order = Order.objects.create(
            user=self.user,
            total_amount=100.0
        )

    def test_invoice_creation(self):
        payment = Payment.objects.create(
            user=self.user,
            amount=50.0,
            success=True
        )
        invoice = Invoice.objects.create(
            order=self.order,
            amount=50.0,
            payment=payment
        )
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(invoice.order, self.order)
        self.assertEqual(invoice.amount, 50.0)
        self.assertEqual(invoice.payment, payment)
