from django.urls import path
from .views import *
urlpatterns = [
    path('/get/team/', CardioView.as_view())
]
