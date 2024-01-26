from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

from ctrl.paggination import CustomIndexPagination
from .serializers import *

# Create your views here.

class AppointmentsView(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer
    pagination_class = CustomIndexPagination


# class AppointmentsView(APIView):
#     def post(self, request):
#         serializer = AppointmentsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'Appointment': serializer.data
#         })
