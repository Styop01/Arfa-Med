from rest_framework import generics
from rest_framework.response import Response

from page.blog.models import Categories, MainBlog
from page.blog.serializers import CategoriesSerializer, MainBlogSerializer
from ctrl.paggination import CustomIndexPagination


# Create your views here.

class BlogView(generics.ListAPIView):
    queryset = MainBlog.objects.all()
    serializer_class = MainBlogSerializer
    pagination_class = CustomIndexPagination


class CategoriesView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = CustomIndexPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        custom_data = {
            'sideBar': {
                "categories": serializer.data
            }
        }
        return Response(custom_data)


# class BlogView(APIView):
#
#     def get(self, request, slug):
#         blog = Blog.objects.all()
#         if slug == "blog":
#             return Response({
#                 "blog": BlogSerializer(blog, many=True).data
#             })
