from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from lenglishonlinelearning import settings
from baseapp.models import Item


class OrderItem(models.Model):
    """Custom model for adding items to the cart"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        """Returns quantity/name"""
        return f"{self.quantity} - {self.item.title}"

    def total_item_price(self):
        """Function calculates item price as per given quantity"""
        return self.quantity * self.item.price

    def final_price(self):
        """Function calculates total price for all items"""
        return self.quantity * self.item.price
    

class Order(models.Model):
    """Custom order model with below fields"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_ref = models.CharField(max_length=20)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey("BillingAddress", on_delete=models.SET_NULL,blank=True, null=True)
    coupon = models.ForeignKey("Coupon", on_delete=models.SET_NULL,blank=True, null=True)
    payment = models.ForeignKey("Payment", on_delete=models.SET_NULL,blank=True, null=True)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        """Function enables display of the username"""
        return self.user.username

    def total_price(self):
        """Total price calculation"""
        total = 0
        for order_item in self.items.all():
            total += order_item.final_price()
        return total

class BillingAddress(models.Model):
    """Custom model for billing address"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    country = CountryField(max_length=100)
    zip = models.CharField(max_length=10)

    def __str__(self):
        """Function enables display of the username"""
        return self.user.username

class Coupon(models.Model):
    """Custom model for coupon"""
    code = models.CharField(max_length=20)
    amount = models.FloatField

    def __str__(self):
        """Function enables display of the coupon name"""
        return self.code

class Payment(models.Model):
    """Custom model for payment"""
    stripe_charge_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestampt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Function enables display of the username"""
        return self.user.username

class Refund(models.Model):
    """Custom model for refund"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk}"
