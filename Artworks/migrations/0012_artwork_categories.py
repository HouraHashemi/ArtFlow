# Generated by Django 4.2.13 on 2024-07-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0011_remove_artwork_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='Artworks.category'),
        ),
    ]
