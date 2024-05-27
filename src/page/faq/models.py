from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.


class Questions(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name="Title"
    )
    body = models.TextField(
        verbose_name="Body"
    )

    def __str__(self):
        return self.title


class FaqHead(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Page Title"
    )
    header = models.CharField(
        max_length=50,
        verbose_name="Header",
        blank=True
    )
    description = RichTextField(
        verbose_name="Description",
    )

    def __str__(self):
        return self.title

