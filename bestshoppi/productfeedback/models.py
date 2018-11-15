from django.db import models
from datetime import date


class CompFeedback(models.Model):
    content = models.CharField(max_length=500, default='')
    date = models.DateField(default=date.today)
    comp_id = models.BigIntegerField()


    def __str__(self):
        return self.content
