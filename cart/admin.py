from django.contrib import admin
from .models import Item, Order, OrderItem, Coupon, Payment, BillingAddress

class SnippetOrderAdmin(admin.ModelAdmin):
    """Admin for snippet"""
    list_display = ['user', 'ordered', 'billing_address', 'payment', 'coupon']
    list_display_links = ['user', 'billing_address', 'payment', 'coupon']


admin.site.register(Item)
admin.site.register(Order, SnippetOrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Coupon)
admin.site.register(Payment)
admin.site.register(BillingAddress)

