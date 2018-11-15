from django.db import models
from subscriptioncategory.models import SubscriptionCategory
from companycategory.models import CompanyCategory
from district.models import District


class CompanyReg(models.Model):

    comp_name = models.CharField(max_length=30, default='')
    email_id = models.CharField(max_length=50, default='')

    address = models.CharField(max_length=100, default='')
    licence_proof = models.CharField(max_length=20, default='')
    comp_decsription = models.CharField(max_length=500, default='')
    comp_image = models.ImageField(upload_to='bestshoppi')
    status = models.BigIntegerField(default='0')
    username = models.CharField(max_length=15, default='')
    password = models.CharField(max_length=15, default='')
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    companycat_id = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)
    subscriptioncat_id = models.ForeignKey(SubscriptionCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.comp_name

