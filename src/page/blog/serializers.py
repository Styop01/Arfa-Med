from rest_framework import serializers

from page.blog.models import Categories, MainBlog


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class MainBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBlog
        fields = "__all__"
