from django import forms
from custregisteration.models import CustomerReg


class LoginForms(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )
    class Meta:
        model = CustomerReg
        fields = ['name']