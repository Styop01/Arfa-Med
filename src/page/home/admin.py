from django.contrib import admin
from .models import *
# from .translations import IconBoxTranslationOptions

# Register your models here.
admin.site.register(IconBox)
admin.site.register(ServiceBox)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Clients)
admin.site.register(Blog)
admin.site.register(Header)


# @admin.register(IconBox)
# class ProductAdmin(IconBoxTranslationOptions):
#     list_display = ("title",)
#
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }
