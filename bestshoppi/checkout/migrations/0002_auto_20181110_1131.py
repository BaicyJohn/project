# Generated by Django 2.0.7 on 2018-11-10 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='ProductName',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='Productid',
        ),
    ]
