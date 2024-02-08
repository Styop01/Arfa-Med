from django.urls import path
from .views import *
urlpatterns = [
    path('get/team/', DoctorsView.as_view())
]
