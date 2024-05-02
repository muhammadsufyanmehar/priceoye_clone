from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'brand', 'category')
    search_fields = ('name', 'brand__name', 'category__name')
    list_filter = ('brand', 'category')
