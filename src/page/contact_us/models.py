from django.db import models

# Create your models here.


class SocialInfo(models.Model):
    SOCIAL_ICON_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('mail', 'Mail'),
        ('linkedin', 'Linkedin'),
    ]
    link = models.URLField()

    icon = models.CharField(
        max_length=20,
        choices=SOCIAL_ICON_CHOICES,
    )

    def __str__(self):
        return self.icon


class ContactInfo(models.Model):
    ICON_CHOICES = [
        ('address', 'Address'),
        ('mail', 'Mail'),
        ('phone', 'Phone'),
        ('hour', 'Hour'),
    ]
    title = models.CharField(
        max_length=20
    )
    subtitle = models.CharField(
        max_length=20
    )
    icon = models.CharField(
        max_length=20,
        choices=ICON_CHOICES,
    )

    def __str__(self):
        return self.icon


class ContactPage(models.Model):
    title = models.CharField(
        max_length=40,
        verbose_name="Page Title"
    )
    header = models.CharField(
        max_length=40,
        verbose_name="Header"
    )
    description = models.CharField(
        max_length=50
    )
    contact_title = models.CharField(
        verbose_name="Contact Info Title",
        max_length=50
    )
    address = models.CharField(
        max_length=40,
    )

class Form(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True
    )
    icon = models.CharField(
        max_length=20
    )
    title = models.CharField(
        max_length=20
    )
    name = models.CharField(
        max_length=20
    )
    type = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return self.icon


# For Message Post


class Message(models.Model):
    your_name = models.CharField(max_length=50)
    your_phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    venue = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.venue

