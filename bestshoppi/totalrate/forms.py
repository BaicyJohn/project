from django import forms
from . import models

class TotalRateForm(forms.ModelForm):
    class Meta:
        model = models.TotalRate
        fields = ['Productid', 'no_item', 'total']
