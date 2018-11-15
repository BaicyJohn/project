from django.db import models
from products.models import Product

# Create your models here.
class Quantity(models.Model):
    Productid = models.BigIntegerField()
    quantity = models.IntegerField(max_length=5)