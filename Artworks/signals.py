from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Artwork
from Users.models import Customer  # Import the Customer model

@receiver(post_save, sender=Artwork)
def add_artwork_to_customer(sender, instance, created, **kwargs):
    if created:
        # Find the customer based on the artwork's owner (user)
        customer = Customer.objects.get(user=instance.owner)
        customer.user_artworks.add(instance)
        customer.save()

@receiver(post_delete, sender=Artwork)
def remove_artwork_from_customer(sender, instance, **kwargs):
    # Find the customer based on the artwork's owner (user)
    customer = Customer.objects.get(user=instance.owner)
    customer.user_artworks.remove(instance)
    customer.save()
