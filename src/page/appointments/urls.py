from django.urls import path
from .views import *
urlpatterns = [
    path('/post/', AppointmentsView.as_view())
]
