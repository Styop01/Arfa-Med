from django.urls import path
from .views import *
urlpatterns = [
    path('get/home/iconbox/', IconBoxView.as_view()),
    path('get/home/servicebox/', ServiceBoxView.as_view()),
    path('get/home/team/', TeamView.as_view()),
    path('get/home/testimonial/', TestimonialView.as_view()),
    path('get/home/clients/', ClientsView.as_view()),
    path('get/home/blog/', BlogView.as_view())
]
