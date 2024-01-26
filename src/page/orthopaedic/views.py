from rest_framework.response import Response
from rest_framework.views import APIView
from page.home.models import Team
from page.home.serializers import TeamSerializer


# Create your views here.
class OrthopaedicView(APIView):
    def get(self, request, slug):
        team = Team.objects.all()
        if slug == "team":
            return Response({
                "orthopaedic": {
                    "team": TeamSerializer(team, many=True).data
                }
            })
