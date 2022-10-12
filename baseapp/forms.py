""" System Module """
from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    """
    Creates product review form
    """
    class Meta:
        """
        Get model and add labels and widgets to the fields
        """
        model = ProductReview
        fields = ('review_text')
        labels = {
            "review_text": "Review",
        }
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 5})
            }