from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AnketaModelViewSet, RatingListAPIView

router = DefaultRouter()
router.register('', AnketaModelViewSet)

urlpatterns = [
    path('anket/', include(router.urls)),
    path('rating/' , RatingListAPIView.as_view())
]