from django.core.exceptions import ValidationError
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Product(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True
    )
    title = models.CharField(
        max_length=50
    )
    price = models.CharField(
        max_length=20
    )


    discount = models.CharField(
        max_length=20,
        blank=True
    )
    description = RichTextField(
        verbose_name="Description",
        null=False,
    )

    def __str__(self):
        return self.title


def validate_image_type(value):
    if value.file.content_type not in ['image/jpeg', 'image/png']:
        raise ValidationError("Image type must be jpg or png")


def validate_image_size(value):
    height = value.height
    width = value.width
    if height != width:
        raise ValidationError(
            "The picture must be portrait(height is equal to width)"
        )


class ProductFooterImages(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Product",
        on_delete=models.CASCADE,
        # related_name='images'
    )
    img = models.ImageField(
        verbose_name="Main Image",
        upload_to='images/products/',
        blank="True",
        validators=[validate_image_size, validate_image_type],
    )

    footer1 = models.ImageField(
        verbose_name="Example 1",
        upload_to='images/devices/products/',
        blank="True",

    )
    footer2 = models.ImageField(
        verbose_name="Example 2",
        upload_to='images/devices/products/',
        blank="True",
    )
    footer3 = models.ImageField(
        verbose_name="Example 3",
        upload_to='images/devices/products/',
        blank="True",
    )
    footer4 = models.ImageField(
        verbose_name="Example 4",
        upload_to='images/devices/products/',
        blank="True",
    )

    # def __str__(self):
    #     return self.id
