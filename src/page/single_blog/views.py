from rest_framework.views import APIView
from rest_framework.response import Response
from page.home.models import Blog
from page.home.serializers import BlogSerializer


# Create your views here.

class SingleView(APIView):

    def get(self, request):
        blog = Blog.objects.all()

        return Response({
            "singleBlog": {
                "blog": BlogSerializer(blog, many=True).data
            }
        })
