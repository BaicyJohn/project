# Generated by Django 2.0.7 on 2018-11-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='ProductName',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
