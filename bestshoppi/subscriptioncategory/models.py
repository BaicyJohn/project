from django.db import models


class SubscriptionCategory(models.Model):
    subcategory_name = models.CharField(max_length=30, default='')
    subcategory_description = models.CharField(max_length=500, default='')
    subcategory_rate = models.IntegerField()

    def __str__(self):
        return self.subcategory_name

