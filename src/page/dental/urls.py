from django.urls import path
from .views import *
urlpatterns = [
    path("get/dental/blog/", DentalView.as_view())
]
