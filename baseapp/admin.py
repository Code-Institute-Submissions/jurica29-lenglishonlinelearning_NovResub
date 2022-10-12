""" System Module """
from django.contrib import admin
from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    """Add below fields for comments"""

    list_display = ["name", "item", "created_at"]


admin.site.register(ProductReview, ProductReviewAdmin)

# class ProductReviewAdmin(admin.ModelAdmin):
#     """
#     Create Order option on admin
#     """
#     list_display = [
#         'user',
#         'date_added',
#         'item',
#         'review_text',
#     ]


# admin.site.register(ProductReview, ProductReviewAdmin)
