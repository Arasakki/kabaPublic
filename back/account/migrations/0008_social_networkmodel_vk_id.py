# Generated by Django 5.0 on 2024-01-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_accountmodel_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='social_networkmodel',
            name='vk_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='VK USER ID'),
        ),
    ]