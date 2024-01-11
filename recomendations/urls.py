
from django.urls import path, include
from .views import RecomendationsListAPIView


urlpatterns = [
    path('', RecomendationsListAPIView.as_view()),
]

