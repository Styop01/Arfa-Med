from django.contrib import admin
from . import models as model
from django.contrib.admin import ModelAdmin

from .models import Form, Message


# Register your models here.
admin.site.register(Message)
admin.site.register(Form)


@admin.register(model.SocialInfo)
class admin_SocialInfo(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"link",
					"icon",
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


@admin.register(model.ContactInfo)
class admin_ContactInfo(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"subtitle",
				]
			},
		),
		(
			"General",
			{
				"fields": [
					"icon",
				]
			},
		),
	]


@admin.register(model.ContactPage)
class admin_ContactPage(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"header",
					"description",
					"contact_title",
					"address",
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
