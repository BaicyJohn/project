from django.db import models


class ProductCategory(models.Model):
    pcategory_name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.pcategory_name
