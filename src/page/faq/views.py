from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.


class FaqView(APIView):

    def get(self, request, slug):
        faq = Questions.objects.all()
        if slug == "questions":
            return Response({
                "faq": {
                    "questions": QuestionsSerializerAll(faq, many=True).data
                }
            })
