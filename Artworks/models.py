# artwork/models.py
from django.db import models
from django.utils import timezone
from django.conf import settings
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return "{}".format(self.name)
    

class ArtworkSize(models.Model):
    hight = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    depth = models.PositiveIntegerField()

    def __str__(self) -> str:
        return "{}x{}x{}".format(self.width, self.hight, self.depth)



class Artwork(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    size = models.CharField(max_length=255, null=True)
    # size = models.ForeignKey('ArtworkSize',on_delete=models.CASCADE, default=ArtworkSize(0,0,0))

    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='artworks/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='categories')
    created_at = models.DateTimeField(default=timezone.now)
    
    SELLING_STATES = [
        ('not_sold', 'not_sold'),
        ('on_auction', 'on_auction'),
        ('pending', 'pending'),
        ('sold_out', 'sold_out'),
    ]
    selling_state = models.CharField(max_length=100,choices=SELLING_STATES, default='not_sold')  # Provide default value
    floor_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # auction_id = models.CharField(max_length=100)


    def __str__(self) -> str:
        return "{}".format(self.title)

