from django.urls import path
from .views import *
urlpatterns = [
    path("about_us/team/", TeamView.as_view()),
    path("about_us/testimonial/", TestimonialView.as_view()),
    path("about_us/clients/", ClientsView.as_view())

]
