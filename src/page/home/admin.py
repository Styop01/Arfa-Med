from django.contrib import admin
from . import models as model
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.
admin.site.register(IconBox)
admin.site.register(ServiceBox)
admin.site.register(Testimonial)
admin.site.register(Header)


@admin.register(model.Slider)
class admin_Slider(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"slogan"
				]
			},
		),
		(
			"General",
			{
				"fields": [
					"image"
				]
			},
		),
	]


@admin.register(model.OurMedical)
class admin_OurMedical(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"slogan",
					"description",
				]
			},
		),
		(
			"General",
			{
				"fields": [
					"image"
				]
			},
		),
	]


