from django.urls import path
from .views import *
urlpatterns = [
    path('/get/<str:slug>/', DoctorsView.as_view())
]
