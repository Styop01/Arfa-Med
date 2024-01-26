from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


# Create your views here.
class FormView(generics.ListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer


class CardView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# class ContactUsView(APIView):
#     def get(self, request, slug):
#         form = Form.objects.all()
#         card = Card.objects.all()
#         return Response({
#             "contact_us": {
#                 "form": FormSerializer(form, many=True).data,
#                 "card": CardSerializer(card, many=True).data
#             }
#         })
#
# # For post Message
#     def post(self, request, slug):
#         serializer = MessageSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         if slug == "message":
#             return Response({
#                 "message": serializer.data
#             })
