# Generated by Django 4.2.7 on 2023-12-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetfood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtruck',
            name='facility_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='foodtruck',
            name='locationid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
