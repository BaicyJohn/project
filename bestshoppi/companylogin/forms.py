from django import forms
from companyregisteration.models import CompanyReg


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
        model = CompanyReg
        fields = ['comp_name']