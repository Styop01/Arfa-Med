from rest_framework import generics

from page.about_us.models import Brand
from page.about_us.serializers import BrandSerializer
from page.home.models import Testimonial
from page.home.serializers import TestimonialSerializer
from ctrl.paggination import CustomIndexPagination


# Create your views here.

class TestimonialView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    pagination_class = CustomIndexPagination


class ClientsView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = CustomIndexPagination

# class AboutUsView(APIView):
#
#     def get(self, request, slug):
#         team = Team.objects.all()
#         testimonial = Testimonial.objects.all()
#         clients = Clients.objects.all()
#
#         if slug == "all":
#             return Response({
#                 "about_us": {
#                     "team": TeamSerializer(team, many=True).data,
#                     "testimonial": TestimonialSerializer(
#                         testimonial, many=True).data,
#                     "clients": ClientsSerializer(clients, many=True).data
#                 }
#             })

