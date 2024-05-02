from rest_framework import viewsets
from shop.models import Product
from shop.serializers import ProductSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer