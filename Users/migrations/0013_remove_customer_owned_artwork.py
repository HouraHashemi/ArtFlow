# Generated by Django 4.2.13 on 2024-07-05 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0012_remove_customer_collected_artwork_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='owned_artwork',
        ),
    ]
