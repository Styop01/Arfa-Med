from django.contrib import admin
from . import models as model
from django.contrib.admin import ModelAdmin


@admin.register(model.AboutUsCreator)
class admin_AboutUsCreator(ModelAdmin):

	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"under_title",
					"image",
					"header",
					"text",
					"certificate",
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


@admin.register(model.Brand)
class admin_Brand(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"img",
				]
			},
		),
		(
			"General",
			{
				"fields": [
					"link",
				]
			},
		),
	]


@admin.register(model.Certificate)
class admin_Certificate(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"image",
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
