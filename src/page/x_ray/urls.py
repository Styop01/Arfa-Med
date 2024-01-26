from django.urls import path
from .views import *
urlpatterns = [
    path("get/x_ray/team/", XrayView.as_view())
]
