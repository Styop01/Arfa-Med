from rest_framework import generics
from .serializers import *
from ctrl.paggination import CustomIndexPagination


# Create your views here.
class IconBoxView(generics.ListAPIView):
    queryset = IconBox.objects.all()
    serializer_class = IconBoxSerializer
    pagination_class = CustomIndexPagination


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
















