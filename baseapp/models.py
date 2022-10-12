""" System Module """
from django.db import models
from django.contrib.auth.models import User
from cart.models import Item


class ProductReview(models.Model):
    """"
    Creates item review
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    review_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return item name on admin panel
        """
        return self.item.name

