from django.urls import path
from .views import *
urlpatterns = [
    path("get/blog/", BlogView.as_view())
]

