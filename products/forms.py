from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import modelformset_factory


class ProductAddForm(ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'strap_color', 'highlight', 'price', 'active_inactive', 'image']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'strap_color': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'highlight': forms.Textarea(attrs={'class': 'form-control', 'required':'true', 'raw':'5'}),
            'price': forms.TextInput(attrs={'type':'number','class': 'form-control', 'required': 'true'}),

        }