from django.urls import path
from .views import *
urlpatterns = [
    path('get/mixins/', DeviceView.as_view())
]
