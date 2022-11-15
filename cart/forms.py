""" System Module """
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class BillingAddressForm(forms.Form):
    """Billing Address form"""

    street_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput",
                "placeholder": "Street and house number",
            }
        )
    )

    apartment_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingApartment",
                "placeholder": "Apartment/House",
            }
        )
    )

    country = CountryField(blank_label="Select Country").formfield(
        widget=CountrySelectWidget(
            attrs={
                "class": "form-control",
                "id": "floatingSelect",
            }
        )
    )

    street_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Street and house number",
            }
        )
    )

    zip_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingZip",
                "placeholder": "Zip code",
            }
        )
    )


class CouponForm(forms.Form):
    """Coupon form"""
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Coupon code"}
        )
    )
