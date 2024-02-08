from rest_framework.response import Response
from rest_framework.views import APIView
from page.home.models import Team
from page.home.serializers import TeamSerializer


# Create your views here.
class DoctorsView(APIView):
    def get(self, request):
        team = Team.objects.all()

        return Response({
            "our_doctors": {
                "team": TeamSerializer(team, many=True).data
            }
        })
