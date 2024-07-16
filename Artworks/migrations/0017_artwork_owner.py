# Generated by Django 4.2.13 on 2024-07-16 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Artworks', '0016_alter_artwork_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
