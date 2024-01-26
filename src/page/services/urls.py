from django.urls import path
from .views import *
urlpatterns = [
    path('get/services/<str:slug>/', ServiceView.as_view())
]
