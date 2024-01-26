from django.urls import path
from .views import *
urlpatterns = [
    path('/get/iconbox/', IconBoxView.as_view()),
    path('/get/servicebox/', ServiceBoxView.as_view()),
    path('/get/team/', TeamView.as_view()),
    path('/get/testimonial/', TestimonialView.as_view()),
    path('/get/clients/', ClientsView.as_view()),
    path('/get/blog/', BlogView.as_view())
]
