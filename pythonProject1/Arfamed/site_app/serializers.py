from rest_framework import serializers
from .models import *


# _______________________________________________________
# aboutUs _______________________________________________
# _______________________________________________________


class AccordionSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = AboutUsAccordion
        fields = "__all__"


class AccordionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsAccordion
        fields = ("img", "title", "body")
# ________________________________________________________
# device _________________________________________________
# ________________________________________________________


class DeviceBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceBanner
        fields = "__all__"


class DeviceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceProduct
        fields = "__all__"
# _________________________________________________________
# sideBar _________________________________________________
# _________________________________________________________


class SideBarCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideBarCategories
        fields = "__all__"


# _________________________________________________________
# servicesSideBar _________________________________________
# _________________________________________________________


class ServiceNavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceNavbar
        fields = "__all__"
# _________________________________________________________
# faq _____________________________________________________
# _________________________________________________________


class FaqQuestionsSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = FaqQuestions
        fields = "__all__"


class FaqQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqQuestions
        fields = ("title", "body")

# ___________________________________________________________
# contactUs _________________________________________________
# ___________________________________________________________


class ContactUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsForm
        fields = "__all__"


class ContactUsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsCard
        fields = "__all__"


# ___________________________________________________________
# GLOBAL ____________________________________________________
# ___________________________________________________________

class GlobalTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalTeam
        fields = "__all__"


class GlobalTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalTestimonial
        fields = "__all__"


class GlobalClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalClients
        fields = "__all__"


class GlobalHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalHeader
        fields = "__all__"


class ForBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForBlog
        fields = "__all__"


# ________________________________________________________
# HOME ___________________________________________________
# ________________________________________________________

class IconBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconBox
        fields = "__all__"


class ServiceBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBox
        fields = "__all__"



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"



class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
