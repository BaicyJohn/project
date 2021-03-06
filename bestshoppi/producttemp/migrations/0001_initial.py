# Generated by Django 2.0.7 on 2018-08-30 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=30)),
                ('product_rate', models.CharField(default='', max_length=30)),
                ('product_description', models.CharField(default='', max_length=500)),
                ('product_image', models.ImageField(upload_to='bestshoppi')),
                ('comp_id', models.BigIntegerField()),
            ],
        ),
    ]
