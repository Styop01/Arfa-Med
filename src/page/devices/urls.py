from django.urls import path
from .views import *

urlpatterns = [
    path('product/get/<str:slug>/<int:pk>/', DeviceView.as_view()),
    path('product/get/<str:slug>/', DeviceView.as_view())
]
