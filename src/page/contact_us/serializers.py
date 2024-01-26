from rest_framework import serializers
from .models import *


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
