from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ctrl.paggination import CustomIndexPagination
from page.home.models import Team
from page.home.serializers import TeamSerializer
from page.services.models import Navbar
from page.services.serializers import NavbarSerializer


# Create your views here.
class ServiceView(generics.ListAPIView):
    pagination_class = CustomIndexPagination

    def get(self, request, *args, **kwargs):
        team = Team.objects.all()
        navbar = Navbar.objects.all()

        serializer1 = TeamSerializer(
            team, context={"request": request}, many=True)
        serializer2 = NavbarSerializer(navbar, many=True)

        custom_data = {
            "services": {
                "team": serializer1.data,
                "navbar": serializer2.data
            }
        }

        return Response(custom_data)
