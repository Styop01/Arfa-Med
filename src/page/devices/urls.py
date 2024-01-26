from django.urls import path
from .views import *
urlpatterns = [
    path('get/devices/list', DeviceView.as_view())
]
