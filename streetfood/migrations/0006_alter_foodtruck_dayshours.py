# Generated by Django 4.2.7 on 2023-12-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetfood', '0005_alter_foodtruck_noisent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruck',
            name='dayshours',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]