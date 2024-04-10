from django.urls import path
from .views import *

urlpatterns = [
    path('get/mixins/', ServiceView.as_view())
]
