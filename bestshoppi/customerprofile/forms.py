from django import forms
from custregisteration.models import CustomerReg


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerReg
        fields = ['name', 'gender', 'dob', 'email', 'contactno', 'username', 'password']

