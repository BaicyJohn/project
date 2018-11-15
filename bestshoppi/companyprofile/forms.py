from django import forms
from companyregisteration.models import CompanyReg


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyReg
        fields = ['comp_name',  'comp_image', 'email_id', 'licence_proof', 'address', 'comp_decsription', 'username', 'password', 'district_id', 'companycat_id', 'subscriptioncat_id']


