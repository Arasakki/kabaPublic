# Generated by Django 5.0 on 2024-01-31 16:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_advertiser', '0012_ad_companymodel_price_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad_companymodel',
            name='ban_show',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=500),
        ),
    ]