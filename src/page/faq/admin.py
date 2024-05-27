from django.contrib import admin
from . import models as model
from django.contrib.admin import ModelAdmin

# Register your models here.

@admin.register(model.Questions)
class admin_Questions(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"body"
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


@admin.register(model.FaqHead)
class admin_FaqHead(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"header",
					"description",
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
