from django.urls import path
from .views import *
urlpatterns = [
    path('get/our_doctors/<str:slug>/', DoctorsView.as_view())
]
