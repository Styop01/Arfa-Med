from rest_framework import generics
from rest_framework.response import Response

from ctrl.paggination import CustomIndexPagination
from page.blog.models import MainBlog
from page.blog.serializers import MainBlogSerializer


# Create your views here.

class SingleView(generics.ListAPIView):
    pagination_class = CustomIndexPagination

    def get(self, request, *args, **kwargs):
        blog = MainBlog.objects.all()
        page = self.paginate_queryset(blog)

        custom_data = {
            "singleBlog": {
                "blog": MainBlogSerializer(page, many=True).data
            }
        }

        return Response(custom_data)
