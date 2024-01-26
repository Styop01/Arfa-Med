from django.urls import path
from .views import *
urlpatterns = [
    path('get/orthopadic<str:slug>/', OrthopaedicView.as_view())
]
