from django.db import models
from datetime import date


class CustomerReg(models.Model):
    name = models.CharField(max_length=30, default='')
    gender = models.CharField(max_length=10, default='')
    dob = models.DateField( default=date.today)
    email = models.CharField(max_length=50, default='')
    contactno = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=30, default='')
    confirm = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name






