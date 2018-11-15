# Generated by Django 2.0.7 on 2018-08-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscriptioncategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(default='', max_length=30)),
                ('subcategory_description', models.CharField(default='', max_length=500)),
                ('subcategory_rate', models.IntegerField()),
            ],
        ),
    ]