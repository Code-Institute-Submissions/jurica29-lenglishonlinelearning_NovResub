from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Contact


class Contact(forms.ModelForm):
    """Contact form"""

    class Meta:
        """Inner class"""

        model = Contact
        fields = ("fullname", "message", "email")

class BillingAddressForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder': 'Street and house number'
    }))

    apartment_address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingApartment',
        'placeholder': 'Apartment/House'
    }))
    
    country = CountryField(blank_label='Select Country').formfield(widget=CountrySelectWidget(attrs={
        'class':'form-control',
        'id':'floatingSelect',
        'placeholder': 'Select country',
        'aria-label': 'Select country'
    }))
    
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder': 'Street and house number'
    }))

    zip_code = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder': 'Zip code'
    }))
    