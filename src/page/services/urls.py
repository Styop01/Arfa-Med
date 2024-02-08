from django.urls import path
from .views import *
urlpatterns = [
    path('get/team/', ServiceView.as_view())
]
