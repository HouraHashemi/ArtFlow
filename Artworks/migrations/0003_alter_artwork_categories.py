# Generated by Django 4.2.13 on 2024-06-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0002_artwork_categories_artwork_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='Artworks.category'),
        ),
    ]
