from django.db import models

# Create your models here.

# devices
# device-product, testimonial, clients, blog,


class Product(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True
    )
    img_path = models.CharField(
        max_length=70, blank=True
    )
    image = models.ImageField(
        upload_to='images/', blank=True
    )
    title = models.CharField(
        max_length=50
    )
    price = models.CharField(
        max_length=20
    )
    discount = models.CharField(
        max_length=20, blank=True
    )

    def __str__(self):
        return self.img_path
