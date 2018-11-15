from . import models
from django import forms


class RegSubscribeForm(forms.ModelForm):
    compname = forms.CharField(
        required=True,
        label='Company Name:',
        max_length=32
    )
    credit_cardno = forms.CharField(
        required=True,
        label='Credit Card No:',
        max_length=32
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )
    class Meta:
        model = models.RegSubscribe
        fields = ['comp_id',  'subscriptioncat_id', 'date', 'time']


