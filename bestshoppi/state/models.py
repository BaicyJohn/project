from django.db import models


class State(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name

