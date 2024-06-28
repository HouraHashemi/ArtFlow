# artwork/models.py
from django.db import models
from artists.models import Artist

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=50)

    SELLING_STATES = [
        ('not_sold', 'not_sold'),
        ('on_auction', 'on_auction'),
        ('sold_out', 'sold_out'),
    ]
    selling_state = models.CharField(max_length=20, choices=SELLING_STATES, default='0')  # Provide default value
    floor_price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)

    auction_id = models.CharField(max_length=100)