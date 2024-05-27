from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from ctrl.paggination import CustomIndexPagination
from .serializers import *

# Create your views here.


# class FaqView(APIView):
#
#     def get(self, request):
#         faq = Questions.objects.all()
#
#         return Response({
#             "faq": {
#                 "questions": QuestionsSerializerAll(faq, many=True).data
#             }
#         })


class FaqView(generics.ListAPIView):

    pagination_class = CustomIndexPagination

    def list(self, request, *args, **kwargs):

        questions = Questions.objects.all()
        page = self.paginate_queryset(questions)
        serializer = QuestionsSerializerAll(page, many=True)
        # for dicts in serializer.data:
        #     appended_title = f'<p><strong>{dicts['title']}</strong></p>'
        #     appended_body = f'<p>{dicts[body]}&nbsp;</p>'
        #     dicts['title'] = appended_title
        #     dicts['body'] = appended_body

        custom_data = {
            'faq': {
                "questions": serializer.data
            }
        }
        return Response(custom_data)
