# Generated by Django 2.0.7 on 2018-08-31 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyregisteration', '0006_remove_companyreg_district_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyreg',
            name='status',
        ),
    ]
