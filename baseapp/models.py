""" System Module """
from django.db import models
from django.contrib.auth.models import User
from cart.models import Item


class ProductReview(models.Model):
    item = models.ForeignKey(Item, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Displaying comment creators names within admin area"""
        return f"{self.item}"

