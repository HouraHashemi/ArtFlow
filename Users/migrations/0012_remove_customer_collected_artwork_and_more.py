# Generated by Django 4.2.13 on 2024-07-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0013_alter_artwork_options_alter_artwork_image'),
        ('Users', '0011_customer_collected_artwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='collected_artwork',
        ),
        migrations.AddField(
            model_name='customer',
            name='owned_artwork',
            field=models.ManyToManyField(related_name='owned_artwork', to='Artworks.artwork'),
        ),
    ]
