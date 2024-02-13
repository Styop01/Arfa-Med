from django.urls import path
from .views import *
urlpatterns = [
    path('get/questions/', FaqView.as_view())
]
