from rest_framework import generics
from rest_framework.response import Response

from ctrl.paggination import CustomIndexPagination
from page.home.models import Blog
from page.home.serializers import BlogSerializer


# Create your views here.

class SingleView(generics.ListAPIView):
    pagination_class = CustomIndexPagination

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.all()
        page = self.paginate_queryset(blog)

        custom_data = {
            "singleBlog": {
                "blog": BlogSerializer(page, many=True).data
            }
        }

        return Response(custom_data)
