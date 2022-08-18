from django.db import models

# Create your models here.

CATEGORY_CHOICES = {
    ('G', 'Group lesson'),
    ('I', 'Individual lesson')
}

LABEL_CHOICES = {
    ('P', 'Package of lessons'),
    ('S', 'Single lesson')
}

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    label = models.CharField(choices=LABEL_CHOICES, max_length=5)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title