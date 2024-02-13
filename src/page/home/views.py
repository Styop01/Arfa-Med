from rest_framework import generics, status
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import (IsAuthenticated,
#                                         IsAuthenticatedOrReadOnly,
#                                         IsAdminUser,
#                                         )
from .serializers import *
from ctrl.paggination import CustomIndexPagination


# Create your views here.
# _____________________________________________________________________________

# Example of multiple model handling with generics
class HomeView(generics.ListAPIView):

    # permission_classes = (IsAuthenticated, )
    pagination_class = CustomIndexPagination
    # authentication_classes = (TokenAuthentication, ) only TokenAuthentication

    def get(self, request, *args, **kwargs):
        # Creating instances for each models
        icon_box = IconBox.objects.all()
        service_box = ServiceBox.objects.all()
        team = Team.objects.all()
        testimonial = Testimonial.objects.all()
        clients = Clients.objects.all()
        blog = Blog.objects.all()
        header = Header.objects.all()

        # pagination for each queryset
        page1 = self.paginate_queryset(icon_box)
        page2 = self.paginate_queryset(service_box)
        page3 = self.paginate_queryset(team)
        page4 = self.paginate_queryset(testimonial)
        page5 = self.paginate_queryset(clients)
        page6 = self.paginate_queryset(blog)
        page7 = self.paginate_queryset(header)

        # instances for each serializer
        serializer1 = ServiceBoxSerializer(page1, many=True)
        serializer2 = ServiceBoxSerializer(page2, many=True)

        serializer3 = TeamSerializer(
            page3, context={'request': request}, many=True
        )

        serializer4 = TestimonialSerializer(page4, many=True)
        serializer5 = ClientsSerializer(page5, many=True)
        serializer6 = BlogSerializer(page6, many=True)
        serializer7 = HeaderSerializer(page7, many=True)

        response_data = {
            'home': {
                'iconbox': serializer1.data,
                'serviceIconBox': serializer2.data,
                'team': serializer3.data,
                'testimonial': serializer4.data,
                'clients': serializer5.data,
                'blog': serializer6.data,
                'header': serializer7.data
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

# _____________________________________________________________________________
class IconBoxView(generics.ListAPIView):
    queryset = IconBox.objects.all()
    serializer_class = IconBoxSerializer
    pagination_class = CustomIndexPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        custom_data = {
            'iconbox': serializer.data
        }
        return Response(custom_data)


class ServiceBoxView(generics.ListAPIView):
    queryset = ServiceBox.objects.all()
    serializer_class = ServiceBoxSerializer
    pagination_class = CustomIndexPagination


class TeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = CustomIndexPagination

class TestimonialView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    pagination_class = CustomIndexPagination


class ClientsView(generics.ListAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    pagination_class = CustomIndexPagination


class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomIndexPagination


# class HomeView(APIView):
#     pagination_class = PageNumberPagination
#
#     def get(self, request, slug, pk):
#         service_box = ServiceBox.objects.all()
#         icon_box = IconBox.objects.all()
#         team = Team.objects.all()
#         testimonial = Testimonial.objects.all()
#         clients = Clients.objects.all()
#         blog = Blog.objects.all()
#         self.pagination_class.page_size = pk
#
#         if slug == "all":
#
#             # Paginate each queryset separately
#             icon_box_page = self.paginate_queryset(icon_box)
#             icon_box_data = IconBoxSerializer(icon_box_page, many=True).data
#
#             service_box_page = self.paginate_queryset(service_box)
#             service_box_data = ServiceBoxSerializer(
#                 service_box_page, many=True).data
#
#             team_page = self.paginate_queryset(team)
#             team_data = TeamSerializer(team_page, many=True).data
#
#             testimonial_page = self.paginate_queryset(testimonial)
#             testimonial_data = TestimonialSerializer(
#                 testimonial_page, many=True).data
#
#             clients_page = self.paginate_queryset(clients)
#             clients_data = ClientsSerializer(clients_page, many=True).data
#
#             blog_page = self.paginate_queryset(blog)
#             blog_data = BlogSerializer(blog_page, many=True).data
#
#             return Response({
#                 "home": {
#                     "iconBox": icon_box_data,
#                     "serviceIconBox": service_box_data,
#                     "team": team_data,
#                     "testimonial": testimonial_data,
#                     "clients": clients_data,
#                     "blog": blog_data
#                 }
#             })
#
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def paginate_queryset(self, queryset):
#         """
#         Paginate the queryset manually.
#         """
#         result_page = self.pagination_class().paginate_queryset(
#             queryset, self.request)
#         return result_page
#

# class HomeView(APIView):
#
#
#     def get(self, request, slug):
#         service_box = ServiceBox.objects.all()
#         icon_box = IconBox.objects.all()
#         team = Team.objects.all()
#         testimonial = Testimonial.objects.all()
#         clients = Clients.objects.all()
#         blog = Blog.objects.all()
#
#         if slug == "all":
#             return Response({
#                 "home": {
#                     "iconBox": IconBoxSerializer(
#                             icon_box, many=True).data,
#                     "serviceIconBox": ServiceBoxSerializer(
#                             service_box, many=True).data,
#                     "team": TeamSerializer(
#                             team, many=True).data,
#                     "testimonial": TestimonialSerializer(
#                             testimonial, many=True).data,
#                     "clients": ClientsSerializer(
#                             clients, many=True).data,
#                     "blog": BlogSerializer(
#                             blog, many=True).data
#                 }
#             })
#         if slug == "testimonial":
#             return Response({
#                 "testimonial": TestimonialSerializer(
#                     testimonial, many=True).data
#             })
















