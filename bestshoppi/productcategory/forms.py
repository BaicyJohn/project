from django import forms
from .import models


class ProductCatForm(forms.ModelForm):
    class Meta:
        model = models.ProductCategory
        fields = ['pcategory_name']