from django import forms
from . import models


class CompRegForm(forms.ModelForm):
    class Meta:
        model = models.CompanyReg
        fields = ['comp_name',  'comp_image', 'email_id', 'licence_proof', 'address', 'comp_decsription', 'username', 'password', 'district_id', 'companycat_id', 'subscriptioncat_id']


