from django.contrib import admin
from .models import Product, ProductFooterImages
from . import models as model
from django.contrib.admin import ModelAdmin

# Register your models here.


@admin.register(model.Product)
class admin_Product(ModelAdmin):
    # list_display = ("id", "img", "title", "price", "discount")
    # list_display_links = list_display

    fieldsets = [
        (
            "English",
            {
                "fields": [
                    "id",
                    "title",
                    "price",
                    "discount",
                    "description",
                ]
            },
        ),
        (
            "General",
            {
                "fields": [
                    # "footer_img1",
                    # "footer_img2",
                    # "footer_img3",
                ]
            },
        ),
    ]


@admin.register(model.ProductFooterImages)
class admin_Product_Images(ModelAdmin):
    # list_display = ("id", "img", "title", "price", "discount")
    # list_display_links = list_display

    fieldsets = [
        (
            "Main Image",
            {
                "fields": [
                    "product",
                    "img",
                ]
            },
        ),
        (
            "Other Examples",
            {
                "fields": [
                    "footer1",
                    "footer2",
                    "footer3",
                    "footer4",
                ]
            },
        ),
    ]
