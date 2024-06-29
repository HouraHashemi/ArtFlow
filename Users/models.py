# # users/models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models



# class User(AbstractUser):
#     pass
#     # is_artist = models.BooleanField(default=False)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True, null=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
#     # collected_artworks = models.ForeignKey('Artworks')
