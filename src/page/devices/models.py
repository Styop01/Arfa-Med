from django.core.exceptions import ValidationError
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
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


class ProductSlider(models.Model):
    title = models.CharField(
        max_length=30
    )
    slogan = models.CharField(
        max_length=40
    )
    image = models.ImageField(
        upload_to='images/devices/product/'
    )

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Product Category"
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Product Name"
    )
    model = models.CharField(
        max_length=30,
        verbose_name="Product Model"
    )
    price = models.CharField(
        max_length=20
    )
    short_description = RichTextField(
        verbose_name="Short Description",
        null=False,
    )
    sku = models.CharField(
        max_length=50,
        verbose_name="SKU"
    )
    category = models.ForeignKey(
        ProductCategory,
        verbose_name="Categories",
        on_delete=models.CASCADE,
    )
    long_description = RichTextField(
        verbose_name="Long Description",
        null=False,
    )
    additional_information = RichTextField(
        verbose_name="Additional Information",
        blank=True
    )

    class Meta:
        verbose_name = "Product",
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name



class ProductImages(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Product",
        on_delete=models.CASCADE,
        # related_name='images'
    )
    image = models.ImageField(
        verbose_name="Image",
        upload_to='images/devices/products/',
        blank="True",
        validators=[validate_image_size, validate_image_type],
    )

    class Meta:
        verbose_name = "Product Image",
        verbose_name_plural = "Product Images"
