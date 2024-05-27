from django.contrib import admin
from . import models as model
from django.contrib.admin import ModelAdmin


# Register your models here.
@admin.register(model.Doctor)
class admin_Doctor(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"name",
					"surname",
					"profession",
					"description",

				]
			},
		),
		(
			"General",
			{
				"fields": [
					"img",
				]
			},
		),
	]


@admin.register(model.DoctorPage)
class admin_DoctorPage(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"header",
					"text",
				]
			},
		),
		(
			"General",
			{
				"fields": [
				]
			},
		),
	]
