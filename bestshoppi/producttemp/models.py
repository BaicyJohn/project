from django.db import models



class Product(models.Model):
    product_name = models.CharField(max_length=30, default='')
    product_rate = models.CharField(max_length=30, default='')
    product_description = models.CharField(max_length=500, default='')
    product_image = models.ImageField(upload_to='bestshoppi')
    comp_id = models.BigIntegerField()



    def __str__(self):
        return self.product_name
