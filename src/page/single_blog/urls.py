from django.urls import path
from .views import *
urlpatterns = [
    path('get/single_blog/blog/', SingleView.as_view())
]
