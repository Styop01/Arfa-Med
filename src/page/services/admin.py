from django.contrib import admin
from . import models as model
from django.contrib.admin import ModelAdmin


@admin.register(model.Navbar)
class admin_Navbar(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"title",
					"link"
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


@admin.register(model.NavbarInfo)
class admin_NavbarInfo(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"navbar",
					"image",
					"title",
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


@admin.register(model.Category)
class admin_Category(ModelAdmin):
	fieldsets = [
		(
			"English",
			{
				"fields": [
					"name",
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
