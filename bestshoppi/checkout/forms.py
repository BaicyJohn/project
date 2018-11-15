from django import forms
from . import models


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = models.Checkout
        fields = [ 'address', 'Email', 'contactno', 'district_id']


