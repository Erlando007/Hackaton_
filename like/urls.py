from django.urls import path
from .views import LikeHistoryListAPIView

urlpatterns = [
    # Другие URL-шаблоны
    path('like_history/', LikeHistoryListAPIView.as_view(), name='like-history'),
]