# Generated by Django 4.2.13 on 2024-07-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0009_alter_artwork_owner'),
        ('Users', '0006_alter_customer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user_artwork',
            field=models.ManyToManyField(related_name='owned_artwork', to='Artworks.artwork'),
        ),
    ]
