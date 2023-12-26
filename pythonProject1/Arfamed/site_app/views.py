from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


# ____________________________________________________ GLOBAL AND HOME _________________________________________________


class GlobalAll(APIView):
    def get(self, request, slug):
        side_categories = SideBarCategories.objects.all()
        global_team = GlobalTeam.objects.all()
        global_test = GlobalTestimonial.objects.all()
        global_clients = GlobalClients.objects.all()
        global_header = GlobalHeader.objects.all()
        for_blog = ForBlog.objects.all()
        icon_box = IconBox.objects.all()
        service_box = ServiceBox.objects.all()
        service_navbar = ServiceNavbar.objects.all()
        device_product = DeviceProduct.objects.all()
        form = ContactUsForm.objects.all()
        card = ContactUsCard.objects.all()
        faq = FaqQuestions.objects.all()

        if slug == "faq":
            return Response({"faq": {"questions": FaqQuestionsSerializerAll(faq, many=True).data}})

        if slug == "contactUs":
            return Response({'contactUs':
                            {"card": ContactUsCardSerializer(card, many=True).data,
                            "form": ContactUsFormSerializer(form, many=True).data}})

        if slug == 'device_product':
            return Response({"device": {"product": DeviceProductSerializer(device_product, many=True).data}})

        if slug == 'navbar':
            return Response({'serviceSideBar': {"navbar": ServiceNavbarSerializer(service_navbar, many=True).data}})

        if slug == "global":
            return Response({"global": {"team": GlobalTeamSerializer(global_team, many=True).data,
                         "testimonial": GlobalTestimonialSerializer(global_test, many=True).data,
                         "clients": GlobalClientsSerializer(global_clients, many=True).data,
                         "header": GlobalHeaderSerializer(global_header, many=True).data,
                         "blog": ForBlogSerializer(for_blog, many=True).data},
                         "home": {"iconBox": IconBoxSerializer(icon_box, many=True).data,
                         "serviceIconBox": ServiceBoxSerializer(service_box, many=True).data},
                         "sideBar": {"categories": SideBarCategoriesSerializer(side_categories, many=True).data}
                         })



# ----------------------------------------------------- VIEW FOR GLOBAL ------------------------------------------------


class GlobalView(APIView):
    def get(self, request, slug):
        global_team = GlobalTeam.objects.all()
        global_test = GlobalTestimonial.objects.all()
        global_clients = GlobalClients.objects.all()
        global_header = GlobalHeader.objects.all()
        for_blog = ForBlog.objects.all()

        if slug == "globalTeam":
            return Response({"team": GlobalTeamSerializer(global_team, many=True).data})

        if slug == "globalTestimonial":
            return Response({"test": GlobalTestimonialSerializer(global_test, many=True).data})

        if slug == "globalClients":
            return Response({"clients": GlobalClientsSerializer(global_clients, many=True).data})

        if slug == "globalHeader":
            return Response({"header": GlobalHeaderSerializer(global_header, many=True).data})

        if slug == "blog":
            return Response({"global": {"blog": ForBlogSerializer(for_blog, many=True).data}})

        if slug == "dataAll":
            return Response({"team": GlobalTeamSerializer(global_team, many=True).data,
                             "testimonial": GlobalTestimonialSerializer(global_test, many=True).data,
                             "clients": GlobalClientsSerializer(global_clients, many=True).data,
                             # "header": GlobalHeaderSerializer(global_header, many=True).data,
                             # "blog": ForBlogSerializer(for_blog, many=True).data,
                             })


class ForBlogAPIList(generics.ListCreateAPIView):
    queryset = ForBlog.objects.all()
    serializer_class = ForBlogSerializer
# ------------------------------------------------------ VIEW FOR HOME -------------------------------------------------


class HomeView(APIView):
    def get(self, request, slug):
        icon_box = IconBox.objects.all()
        service_box = ServiceBox.objects.all()

        if slug == "iconBox":
            return Response({"iconBox": IconBoxSerializer(icon_box, many=True).data})

        if slug == "serviceIconBox":
            return Response({"serviceIconBox": ServiceBoxSerializer(service_box, many=True).data})

        if slug == "dataAll":
            return Response({"iconBox": IconBoxSerializer(icon_box, many=True).data,
                             "serviceIconBox": ServiceBoxSerializer(service_box, many=True).data})


#_______Post views_______

class AppointmentsAPIList(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer


class MessageAPIList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers




# __________Delete views_______

class AppointmentsAPIDelete(generics.DestroyAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer


class MessageAPIDelete(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers