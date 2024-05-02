from rest_framework import viewsets
from payments.models import Payment, Invoice
from payments.serializers import PaymentDetialSerializer, InvoiceDetailSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentDetialSerializer
    queryset = Invoice.objects.all()
    serializer_class = InvoiceDetailSerializer