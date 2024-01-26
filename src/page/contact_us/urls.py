from django.urls import path
from .views import *
urlpatterns = [
    path("/get/form/", FormView.as_view()),
    path("/get/card/", CardView.as_view()),
    path("/get/message/", MessageView.as_view())
]
