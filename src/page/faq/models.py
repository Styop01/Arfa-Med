from django.db import models

# Create your models here.


class Questions(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    toggle = models.CharField(max_length=20, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title
