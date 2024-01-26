from django.urls import path
from .views import *
urlpatterns = [
    path("/get/team/", XrayView.as_view())
]
