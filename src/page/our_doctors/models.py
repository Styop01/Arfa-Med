from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Doctor(models.Model):
	img = models.ImageField(
		upload_to='images/doctors/'
	)
	name = models.CharField(
		max_length=50
	)
	surname = models.CharField(
		max_length=50
	)
	profession = models.CharField(
		max_length=50
	)
	description = RichTextField(
		verbose_name="Doctor Description",
		null=False,
	)

	def __str__(self):
		return self.name


class DoctorPage(models.Model):
	title = models.CharField(
		max_length=50,
		verbose_name="Page Title"
	)
	header = models.CharField(
		max_length=50,
		verbose_name="Header"
	)
	text = models.CharField(
		max_length=50,
		verbose_name="Text"
	)

	def __str__(self):
		return self.title
