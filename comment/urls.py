from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentListCreateAPIView


urlpatterns = [
    path('', CommentListCreateAPIView.as_view())
]