""" System Module """
from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    """Class used for review form"""

    class Meta:
        """Inner class"""

        model = ProductReview
        fields = ("review_text",)
        # Fixing the size of comment box
        widgets = {
            "review_text": forms.Textarea(attrs={"rows": 10, "cols": 80}),
        }
        labels = {
            "review_text": ""
        }

