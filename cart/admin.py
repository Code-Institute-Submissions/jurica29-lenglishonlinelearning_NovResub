from django.contrib import admin
from .models import Order, OrderItem, Coupon, Payment, BillingAddress, Refund

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Coupon)
admin.site.register(Payment)
admin.site.register(BillingAddress)
admin.site.register(Refund)
