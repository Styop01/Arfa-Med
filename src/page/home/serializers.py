from rest_framework import serializers
from .models import *


class IconBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconBox
        fields = "__all__"


class ServiceBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBox
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = "__all__"
