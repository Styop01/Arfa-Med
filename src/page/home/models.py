from django.db import models
# from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


# Create your models here.


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


class Team(models.Model):

    id = models.PositiveIntegerField(
        primary_key=True
    )

    img = models.TextField(
        max_length=100
    )

    content = models.CharField(
        max_length=50
    )

    title = models.CharField(
        max_length=50
    )


    def __str__(self):
        return self.content


class Testimonial(models.Model):

    id = models.IntegerField(
        primary_key=True
    )

    img = models.CharField(
        max_length=50
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


class Clients(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True
    )

    img = models.CharField(
        max_length=50
    )

    hover = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.hover


class Blog(models.Model):

    id = models.PositiveIntegerField(
        primary_key=True
    )

    img = models.CharField(
        max_length=20
    )

    dateAttr = models.CharField(
        max_length=30
    )

    day = models.PositiveIntegerField()

    month = models.CharField(
        max_length=10
    )

    year = models.PositiveIntegerField()

    commCount = models.IntegerField()

    publisher = models.CharField(
        max_length=20
    )

    title = models.CharField(
        max_length=50
    )

    to = models.CharField(
        max_length=10
    )

    subtitle = models.TextField()

    single = models.TextField()

    def __str__(self):
        return self.title


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
