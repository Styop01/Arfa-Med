from django.urls import path
from .views import *

urlpatterns = [
    # For Home Global
    path('get/<str:slug>/', GlobalAll.as_view()),
    # For Global -------------------------------------------------------------
    path('get/global/<str:slug>/', GlobalView.as_view()),
    path('global/post', GlobalView.as_view()),
    # For Home ---------------------------------------------------------------
    path("get/home/<str:slug>/", HomeView.as_view()),
    path('post/appointment/', AppointmentsAPIList.as_view()),
    path('post/message/', MessageAPIList.as_view()),
    path('delete/appointment/<int:pk>/', AppointmentsAPIDelete.as_view()),
    path('delete/message/<int:pk>/', MessageAPIDelete.as_view()),
]
