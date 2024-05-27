from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Navbar(models.Model):
	title = models.CharField(
		max_length=30
	)
	link = models.CharField(
		max_length=30
	)

	def __str__(self):
		return self.title


class NavbarInfo(models.Model):
	navbar = models.ForeignKey(
		Navbar,
		verbose_name="Navbar",
		on_delete=models.CASCADE,
	)
	image = models.ImageField(
		verbose_name='Image',
		upload_to='images/services/',
		blank=True
	)
	title = models.CharField(
		verbose_name='Title',
		max_length=50,
		blank=True
	)
	description = RichTextField(
		verbose_name='Description',
	)

	def __str__(self):
		return self.title


class Category(models.Model):
	name = models.CharField(
		verbose_name='Category',
		max_length=100,
	)

	def __str__(self):
		return self.name


class Advertisement(models.Model):
	title = models.CharField(
		verbose_name='Title',
		max_length=30
	)
	description = models.TextField(
		verbose_name='Description',
		blank=True
	)
	url = models.URLField()

	def __str__(self):
		return self.title

