from rest_framework.response import Response
from rest_framework.views import APIView

from page.our_doctors.models import Doctor
from page.our_doctors.serializers import DoctorSerializer


# Create your views here.
class DoctorsView(APIView):
    def get(self, request):
        team = Doctor.objects.all()

        return Response({
            "our_doctors": {
                "team": DoctorSerializer(team, many=True).data
            }
        })
