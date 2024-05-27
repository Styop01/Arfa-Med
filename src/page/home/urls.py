
from django.urls import path, include, re_path

from core import settings
from .views import *
# from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('get/iconbox/', IconBoxView.as_view()),
    path('get/servicebox/', ServiceBoxView.as_view()),
    path('get/testimonial/', TestimonialView.as_view()),
    path('get/clients/', ClientsView.as_view()),
    path('get/blog/', BlogView.as_view()),
    path('get/mixins/', HomeView.as_view()),

]
