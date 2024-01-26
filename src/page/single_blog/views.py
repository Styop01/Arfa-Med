from rest_framework.views import APIView
from rest_framework.response import Response
from page.home.models import Blog
from page.home.serializers import BlogSerializer


# Create your views here.

class SingleView(APIView):

    def get(self, request, slug):
        blog = Blog.objects.all()

        return Response({
            "single_blog": {
                "blog": BlogSerializer(blog, many=True).data
            }
        })
