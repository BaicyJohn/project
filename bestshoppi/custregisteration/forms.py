from django import forms
from .import models


class CustRegForm(forms.ModelForm):

    #password = forms.CharField(widget=forms.PasswordInput)
   # password2 = forms.CharField(widget=forms.PasswordInput)
   # email = forms.EmailField(max_length=50)
    class Meta:
        model = models.CustomerReg
        fields = ['name', 'gender', 'dob', 'email', 'contactno', 'username', 'password', 'confirm']