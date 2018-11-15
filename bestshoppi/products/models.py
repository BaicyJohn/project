from django.db import models
from productcategory.models import ProductCategory


class Product(models.Model):
    product_name = models.CharField(max_length=30, default='')
    product_rate = models.CharField(max_length=30, default='')
    product_description = models.CharField(max_length=500, default='')
    product_image = models.ImageField(upload_to='bestshoppi')
    comp_id = models.BigIntegerField()
    productcat_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
