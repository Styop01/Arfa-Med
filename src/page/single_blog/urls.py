from django.urls import path
from .views import *
urlpatterns = [
    path('/get/blog/', SingleView.as_view())
]
