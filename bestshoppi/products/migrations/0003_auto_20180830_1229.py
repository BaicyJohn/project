# Generated by Django 2.0.7 on 2018-08-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='comp_id',
            field=models.BigIntegerField(),
        ),
    ]