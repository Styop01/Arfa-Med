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


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = "__all__"
