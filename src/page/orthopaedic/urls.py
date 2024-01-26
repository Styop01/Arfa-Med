from django.urls import path
from .views import *
urlpatterns = [
    path('/get/<str:slug>/', OrthopaedicView.as_view())
]
