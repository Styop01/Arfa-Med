from django.urls import path
from .views import *
urlpatterns = [
    path("/get/", BlogView.as_view())
]

