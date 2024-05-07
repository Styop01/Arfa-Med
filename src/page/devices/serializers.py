from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "price", "discount")

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFooterImages
        fields = ("id", "img", "footer1", "footer2", "footer3", "footer4",)


class PaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFooterImages
        fields = ("img",)

