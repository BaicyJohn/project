from django import forms
from . import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['product_name', 'product_rate', 'product_description', 'product_image', 'comp_id', 'productcat_id']
