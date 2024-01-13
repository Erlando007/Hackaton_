from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AnketaModelViewSet, RatingListAPIView
from like.views import LikeHistoryListAPIView

from .views import *


r
router = DefaultRouter()
router.register('', AnketaModelViewSet)

urlpatterns = [
    path('anket/', include(router.urls)),
    path('rating/' , RatingListAPIView.as_view()),
    path('like_history/', LikeHistoryListAPIView.as_view(), name='like_history_api')
]
