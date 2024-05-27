from django.urls import path
from .views import *

urlpatterns = [
    path("get/testimonial/", TestimonialView.as_view()),
    path("get/clients/", ClientsView.as_view())

]
