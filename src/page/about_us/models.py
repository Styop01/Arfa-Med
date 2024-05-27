from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class AboutUsCreator(models.Model):
	title = models.CharField(
		max_length=20,
		verbose_name="Page Title",
		blank=False
	)
	under_title = models.CharField(
		max_length=20,
		verbose_name="Page Under Title",
		blank=True
	)
	image = models.ImageField(
		verbose_name="Image",
		upload_to='images/about_us/'
	)
	header = models.CharField(
		max_length=40,
		verbose_name="Header",
	)
	description = RichTextField(
		verbose_name="Description"
	)

	def __str__(self):
		return self.title


class Certificate(models.Model):
	image = models.ImageField(
		verbose_name="Certificate Image",
		upload_to='images/about_us/'
	)

	def __str__(self):
		return self.image


class Brand(models.Model):
	img = models.ImageField(
		upload_to='images/about_us/',
		verbose_name="Brand Image"
	)
	link = models.URLField(
		verbose_name="Brand Link"
	)

	def __str__(self):
		return self.link

