# Generated by Django 2.0.7 on 2018-11-10 05:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Custid', models.CharField(max_length=10)),
                ('Productid', models.BigIntegerField()),
                ('ProductName', models.CharField(max_length=10)),
                ('Grandtotal', models.IntegerField()),
                ('dob', models.DateField(default=datetime.date.today)),
                ('Email', models.CharField(max_length=20)),
                ('contactno', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=30)),
                ('orderno', models.CharField(max_length=10)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.District')),
            ],
        ),
    ]
