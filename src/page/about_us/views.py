from rest_framework import generics
from page.home.models import Team, Testimonial, Clients
from page.home.serializers import TeamSerializer, TestimonialSerializer, \
    ClientsSerializer
from ctrl.paggination import CustomIndexPagination


# Create your views here.
class TeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [CustomIndexPagination]


class TestimonialView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [CustomIndexPagination]


class ClientsView(generics.ListAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [CustomIndexPagination]

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

