from ckeditor.fields import RichTextField
from django.db import models

from django.utils.translation import gettext_lazy as _


# Create your models here.

class Slider(models.Model):
    image = models.ImageField(
        upload_to='images/home/',
        verbose_name='Background Image'
    )
    title = models.CharField(
        max_length=45,
        verbose_name='Title'
    )
    slogan = models.CharField(
        max_length=70,
        verbose_name='Slogan'
    )

    def __str__(self):
        return self.title


class OurMedical(models.Model):
    image = models.ImageField(
        upload_to='images/home/',
        verbose_name='Image'
    )
    title = models.CharField(
        max_length=60,
        verbose_name='Title'
    )
    slogan = models.CharField(
        max_length=30,
        verbose_name='Slogan'
    )
    description = RichTextField(
        verbose_name='Description',

    )

    def __str__(self):
        return self.title


# About Medical ????_________________________________________________________

class IconBox(models.Model):

    id = models.PositiveIntegerField(
        primary_key=True
    )
    # description = RichTextField(_("Description"), null=False)
    icon = models.CharField(
        unique=True,
        max_length=70,
    )
    title = models.CharField(
        unique=True,
        max_length=70
    )
    subtitle = models.TextField(
        max_length=250
    )

    def __str__(self):
        return self.title


class ServiceBox(models.Model):

    id = models.PositiveIntegerField(
        primary_key=True
    )
    icon = models.CharField(
        unique=True,
        max_length=30
    )
    title = models.CharField(
        unique=True,
        max_length=30
    )
    subtitle = models.TextField(
        max_length=250
    )

    def __str__(self):
        return self.title


class Testimonial(models.Model):

    id = models.IntegerField(
        primary_key=True
    )
    img = models.ImageField(
        upload_to='images/'
    )

    name = models.CharField(
        max_length=30
    )
    subtitle = models.CharField(
        max_length=30
    )
    body = models.TextField()

    def __str__(self):
        return self.name


class Header(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True
    )

    title = models.CharField(
        max_length=20
    )

    link = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.title
