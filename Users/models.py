from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib import admin
from Artworks.models import Artwork

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # artistic_name 


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_artwork = models.ManyToManyField(Artwork, related_name='user_artwork')

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
    
    # collected_artwork = models.ManyToManyField(Artwork, related_name='collected_artwork')
    # auction_artwork = models.ManyToManyField(Artwork, related_name='auction_artwork')
    

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('allow_add_artwork', 'Can add new Artwork'),
            ('allow_change_artwork', 'Can change existed Artwork')
        ]

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)