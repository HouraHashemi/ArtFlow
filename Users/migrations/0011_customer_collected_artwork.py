# Generated by Django 4.2.13 on 2024-07-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0013_alter_artwork_options_alter_artwork_image'),
        ('Users', '0010_alter_customer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='collected_artwork',
            field=models.ManyToManyField(related_name='collected_artwork', to='Artworks.artwork'),
        ),
    ]
