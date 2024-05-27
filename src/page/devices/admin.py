from django.contrib import admin
from .models import *
from . import models as model
from django.contrib.admin import ModelAdmin

# Register your models here.

@admin.register(model.ProductSlider)
class admin_ProductSlider(ModelAdmin):
    fieldsets = [
        (
            "English",
            {
                "fields": [
                    "title",
                    "slogan",
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


@admin.register(model.ProductCategory)
class admin_ProductCategory(ModelAdmin):
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


class ProductImages(admin.TabularInline):
    model = model.ProductImages


@admin.register(model.Product)
class admin_Product(ModelAdmin):
    # list_display = ("product", "image")
    inlines = [ProductImages]
    # list_display_links = list_display
    fieldsets = [
        (
            "English",
            {
                "fields": [
                    "name",
                    "model",
                    "price",
                    "short_description",

                    "long_description",
                    "additional_information"
                ]
            },
        ),
        (
            "General",
            {
                "fields": [
                    "sku",
                    "category",
                ]
            },
        ),


    ]


# @admin.register(model.ProductFooterImages)
# class admin_Product_Images(ModelAdmin):
#     # list_display = ("id", "img", "title", "price", "discount")
#     # list_display_links = list_display
#
#     fieldsets = [
#         (
#             "Main Image",
#             {
#                 "fields": [
#                     "product",
#                     "img",
#                 ]
#             },
#         ),
#         (
#             "Other Examples",
#             {
#                 "fields": [
#                     "footer1",
#                     "footer2",
#                     "footer3",
#                     "footer4",
#                 ]
#             },
#         ),
#     ]
