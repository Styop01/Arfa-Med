from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Categories(models.Model):
	text = models.CharField(
		max_length=20
	)
	number = models.CharField(
		max_length=20
	)

	def __str__(self):
		return self.text


class Advertisement(models.Model):
	title = models.CharField(
		verbose_name='Title',
		max_length=30
	)
	description = models.TextField(
		verbose_name='Description',
		blank=True
	)
	url = models.URLField(),
	image = models.ImageField(
		upload_to='images/blog/'
	)

	def __str__(self):
		return self.title


class MainBlog(models.Model):
	img = models.ImageField(
		upload_to='images/blog/',
		verbose_name='Image'
	)
	publish_date = models.DateField(
		verbose_name="Publish Date"
	)
	publisher = models.CharField(
		max_length=20
	)
	category = models.ForeignKey(
		Categories, on_delete=models.CASCADE
	)
	title = models.CharField(
		max_length=50
	)
	subtitle = RichTextField(
		verbose_name="Blog Description",
		null=False,
	)

	def __str__(self):
		return self.title

