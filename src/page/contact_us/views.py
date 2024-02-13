from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.permissions import (IsAuthenticated,
#                                         IsAuthenticatedOrReadOnly,
#                                         IsAdminUser,
#                                         )

from ctrl.paggination import CustomIndexPagination
from .serializers import *


# Create your views here.
class FormView(generics.ListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer


class CardView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class MixinsView(generics.ListAPIView):

    pagination_class = CustomIndexPagination
    # permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        card = Card.objects.all()
        form = Form.objects.all()

        page1 = self.paginate_queryset(card)
        page2 = self.paginate_queryset(form)

        serializer1 = CardSerializer(page1, many=True)
        serializer2 = FormSerializer(page2, many=True)

        custom_data = {
            "contactUs": {
                "card": serializer1.data,
                "form": serializer2.data,
            }
        }

        return Response(custom_data)


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
