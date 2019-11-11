"""Forms for order application."""

import datetime
import re

from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from product.models import Product, ProductImages


class ProductForm(forms.ModelForm):
    """Product model mapped form."""

    class Meta:
        """Specify fields to include."""

        model = Product
        fields = '__all__'

    def clean_title(self):
        """Check if title is valid."""
        title = self.cleaned_data['title']

        if not self._validate_text(title):
            raise ValidationError(('Invalid title.'))

        return title

    def clean_product_type(self):
        """Check if type is valid."""
        product_type = self.cleaned_data['product_type']

        if not self._validate_text(product_type):
            raise ValidationError(('Invalid product_type.'))

        return product_type

    def _validate_text(self, text):
        """Match valid text regex with text field."""
        return bool(re.match(
            r'^[_A-z]*((-|\s)*[_A-z])*$',
            str(text)
        ))


class ProductImagesForm(forms.ModelForm):
    """Product image model mapped form."""

    class Meta:
        """Meta for PI."""

        model = ProductImages
        exclude = ('product',)
