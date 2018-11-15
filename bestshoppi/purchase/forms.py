from django import forms
from . import models

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = models.Purchase
        fields = ['no_item']
