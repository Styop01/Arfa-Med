from django.contrib import admin
from . import models as model
from django.contrib.admin import ModelAdmin


# Register your models here.


@admin.register(model.Categories)
class admin_Categories(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"text",
					"number"
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


@admin.register(model.Advertisement)
class admin_Advertisement(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"description",
					"url",
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


@admin.register(model.MainBlog)
class admin_MainBlog(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"img",
					"publisher",
					"publish_date",
					"category",
					"title",
					"subtitle",

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

