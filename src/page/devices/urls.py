from django.urls import path
from .views import *
urlpatterns = [
    path('/get/list', DeviceView.as_view())
]
