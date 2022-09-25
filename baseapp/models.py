from django.db import models
from django.shortcuts import reverse


CATEGORY_CHOICES = {
    ('C', 'Course'),
    ('L', 'Lesson')
}

LABEL_CHOICES = {
    ('P', 'Package of lessons'),
    ('S', 'Single lesson')
}

class Item(models.Model):
    """Custom item model with below fields"""
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    label = models.CharField(choices=LABEL_CHOICES, max_length=5)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        """Function enables display of the item title"""
        return self.title

    def get_item_url(self):
        """Function enables display of product detail page"""
        return reverse('baseapp:detail', kwargs={
            'slug':self.slug
        })

    def get_add_to_cart(self):
        return reverse('cart:add-to-cart', kwargs={
            'slug': self.slug
        })
        
    def snip_description(self):
        return self.description[:30] + "..."