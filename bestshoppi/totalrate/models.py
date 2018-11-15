from django.db import models
from products.models import Product


class TotalRate(models.Model):
    Productid = models.BigIntegerField()
    no_item = models.IntegerField(max_length=5)
    total = models.IntegerField(max_length=8)