from rest_framework import generics
from rest_framework.response import Response
from ctrl.paggination import CustomIndexPagination
from page.home.models import Blog, Testimonial, Clients
from .serializers import *
from page.home.serializers import (BlogSerializer, TestimonialSerializer,
                                   ClientsSerializer,)


# Create your views here.
class DeviceView(generics.ListAPIView):

    pagination_class = CustomIndexPagination

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        testimonial = Testimonial.objects.all()
        clients = Clients.objects.all()
        blog = Blog.objects.all()

        page1 = self.paginate_queryset(product)
        page2 = self.paginate_queryset(testimonial)
        page3 = self.paginate_queryset(clients)
        page4 = self.paginate_queryset(blog)

        serializer1 = ProductSerializer(page1, many=True)
        serializer2 = TestimonialSerializer(page2, many=True)
        serializer3 = ClientsSerializer(page3, many=True)
        serializer4 = BlogSerializer(page4, many=True)

        custom_data = {
            "devices" : {
                "product" : serializer1.data,
                "testimonial" : serializer2.data,
                "clients" : serializer3.data,
                "blog" : serializer4.data
            }
        }

        return Response(custom_data)

