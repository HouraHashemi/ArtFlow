from django.db import models
from Artworks.models import Artwork
from django.utils import timezone
from django.conf import settings



class Bid(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)
    bid_price = models.PositiveIntegerField(default=0)
    is_valid = models.BooleanField(default=False)



class Auction(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    bids = models.ManyToManyField(Bid, related_name='bids')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    collector = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)





