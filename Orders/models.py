# orders/models.py
from django.db import models
from users.models import User
from artwork.models import Artwork
from auction.models import Auction

class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    auction = models.ForeignKey(Auction, related_name='auction')


# transactions