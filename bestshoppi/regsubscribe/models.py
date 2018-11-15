from django.db import models
from datetime import date, time

from subscriptioncategory.models import SubscriptionCategory

# Create your models here.
class RegSubscribe(models.Model):
    comp_id = models.BigIntegerField(default='0')
    subscriptioncat_id = models.ForeignKey(SubscriptionCategory, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=time.today)