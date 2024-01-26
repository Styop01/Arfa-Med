from django.urls import path
from .views import *
urlpatterns = [
    path("get/contact_us/form/", FormView.as_view()),
    path("get/contact_us/card/", CardView.as_view()),
    path("get/contact_us/message/", MessageView.as_view())
]
