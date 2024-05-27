from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "price", "discount")

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "all"



