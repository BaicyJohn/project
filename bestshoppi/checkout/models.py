from django.db import models
from products.models import Product
from custregisteration.models import CustomerReg
from district.models import District

from datetime import date


class Checkout(models.Model):
    Custid = models.CharField(max_length=10)
    Grandtotal = models.IntegerField()
    dob = models.DateField(default=date.today)
    Email = models.CharField(max_length=20)
    contactno = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=30, default='')
    orderno=models.CharField(max_length=10)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
