from django.db import models

# Create your models here.
class Auction(models.Model):
    #     id = models.CharField(primary_key=True, default=generate_random_id, max_length=6, unique=True)

    # def save(self, *args, **kwargs):
    # if not self.id:
    #     # Generate a unique alphanumeric ID
    #     while True:
    #         random_id = generate_random_id()
    #         if not MyModel.objects.filter(id=random_id).exists():
    #             self.id = random_id
    #             break
    # super().save(*args, **kwargs)
    pass
