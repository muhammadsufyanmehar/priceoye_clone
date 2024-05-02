from django.contrib import admin
from .models import Payment, Invoice

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'timestamp', 'success')
    search_fields = ('user__username', 'timestamp')
    list_filter = ('timestamp', 'success')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment')
    search_fields = ('order__user__username',)
    list_filter = ('amount',)
