from rest_framework import generics
from page.home.models import Team
from page.home.serializers import TeamSerializer
from ctrl.paggination import CustomIndexPagination


# Create your views here.

class CardioView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = CustomIndexPagination




# class CardioView(APIView):
#     def get(self, request, slug):
#         team = Team.objects.all()
#         if slug == "team":
#             return Response({
#                 "cardio": {
#                     "team": TeamSerializer(team, many=True).data
#                 }
#             })
