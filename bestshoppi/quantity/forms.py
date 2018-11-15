from django import forms
from . import models

class QuantityForm(forms.ModelForm):
    class Meta:
        model = models.Quantity
        fields = ['quantity']
