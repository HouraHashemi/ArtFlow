from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib import admin

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # is_artist = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Profile
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # collected_artworks = models.ForeignKey('Artworks')

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('allow_bidding', 'Allow Bidding on an Art')
        ]

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)