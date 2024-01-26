from django.urls import path
from .views import *
urlpatterns = [
    path('get/faq/<str:slug>/', FaqView.as_view())
]
