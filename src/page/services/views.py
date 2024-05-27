from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ctrl.paggination import CustomIndexPagination
from page.our_doctors.models import Doctor
from page.our_doctors.serializers import DoctorSerializer
from page.services.models import Navbar
from page.services.serializers import NavbarSerializer


# Create your views here.
class ServiceView(generics.ListAPIView):
    pagination_class = CustomIndexPagination

    def get(self, request, *args, **kwargs):
        team = Doctor.objects.all()
        navbar = Navbar.objects.all()

        serializer1 = DoctorSerializer(
            team, context={"request": request}, many=True)
        serializer2 = NavbarSerializer(navbar, many=True)

        custom_data = {
            "services": {
                "team": serializer1.data,
                "navbar": serializer2.data
            }
        }

        return Response(custom_data)
