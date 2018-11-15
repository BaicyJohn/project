from django import forms
from .import models


class CompCatForm(forms.ModelForm):
    class Meta:
        model = models.CompanyCategory
        fields = ['category_name', 'category_description']