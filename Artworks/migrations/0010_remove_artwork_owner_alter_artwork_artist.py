# Generated by Django 4.2.13 on 2024-07-02 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Artworks', '0009_alter_artwork_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='owner',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
