""" System Module """
from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    """Class used for comment form"""

    class Meta:
        """Inner class"""

        model = ProductReview
        fields = ("name", "review_text")
        # Fixing the size of comment box
        widgets = {
            "review_text": forms.Textarea(attrs={"rows": 5, "cols": 30}),
        }
        labels = {
            "name": "",
            "review_text": ""
        }

