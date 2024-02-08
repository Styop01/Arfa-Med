from django.db import models

# Create your models here.


class Form(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.icon


class Card(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.TextField(max_length=20)
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)

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

