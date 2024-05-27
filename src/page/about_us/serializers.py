from rest_framework import serializers
from .models import *


# class AboutUsCreatorSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = AboutUsCreator
# 		fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = "__all__"
