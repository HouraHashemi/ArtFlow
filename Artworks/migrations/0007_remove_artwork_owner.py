# Generated by Django 4.2.13 on 2024-06-30 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0006_artwork_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='owner',
        ),
    ]
