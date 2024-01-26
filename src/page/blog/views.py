from rest_framework import generics
from page.home.models import Blog
from page.home.serializers import BlogSerializer
from ctrl.paggination import CustomIndexPagination


# Create your views here.

class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomIndexPagination

# class BlogView(APIView):
#
#     def get(self, request, slug):
#         blog = Blog.objects.all()
#         if slug == "blog":
#             return Response({
#                 "blog": BlogSerializer(blog, many=True).data
#             })
