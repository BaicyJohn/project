from django.db import models


class CompanyCategory(models.Model):
    category_name = models.CharField(max_length=30, default='')
    category_description = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.category_name
