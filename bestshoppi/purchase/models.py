from django.db import models
from products.models import Product
from custregisteration.models import CustomerReg
from datetime import date


class Purchase(models.Model):
    Custid=models.CharField(max_length=10)
    Productid = models.BigIntegerField()
    ProductName=models.CharField(max_length=10)
    no_item = models.IntegerField(max_length=5)
    total = models.BigIntegerField()
    dob = models.DateField(default=date.today)
    orderno = models.CharField(max_length=10, default='101')
    status = models.IntegerField(max_length=2, default=0)
