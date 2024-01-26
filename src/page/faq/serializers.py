from rest_framework import serializers
from .models import *


class QuestionsSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ("title", "body")
