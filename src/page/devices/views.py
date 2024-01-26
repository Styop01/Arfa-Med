from rest_framework.views import APIView
from rest_framework.response import Response


from page.home.models import Blog, Testimonial, Clients
from .serializers import *
from page.home.serializers import (BlogSerializer, TestimonialSerializer,
                                   ClientsSerializer,)


# Create your views here.

class DeviceView(APIView):

    def get(self, request, slug):
        products = Product.objects.all()
        testimonial = Testimonial.objects.all()
        clients = Clients.objects.all()
        blog = Blog.objects.all()

        if slug == "all":
            return Response({
                "devices": {
                    "product": ProductSerializer(
                        products, many=True).data,
                    "testimonial": TestimonialSerializer(
                        testimonial, many=True).data,
                    "clients": ClientsSerializer(
                        clients, many=True).data,
                    "blog": BlogSerializer(
                        blog, many=True).data
                }
            })

