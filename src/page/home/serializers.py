from rest_framework import serializers
from .models import *

#
# class TestSerializerAll(serializers.ModelSerializer):
#     class Meta:
#         model = TestModel
#         fields = '__all__'
#
# class TestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TestModel
#         fields = ('image',)

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

        # def get_photo_url(self, obj):
        #     request = self.context.get("request")
        #     photo_url = obj.fingerprint.url
        #     return request.build_absolute_uri(photo_url)


# class SnippetSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Team
#         fields = ['id', 'img', 'content', 'title', 'owner',]


# class TeamSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Team
#         fields = "__all__"


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
