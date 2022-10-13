""" System Module """
from django.contrib import admin
from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    """Add below fields for comments"""

    list_display = ["item", "created_at"]


admin.site.register(ProductReview, ProductReviewAdmin)


