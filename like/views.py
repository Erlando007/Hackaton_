from rest_framework import generics

from account.models import Anketa
from .models import LikeHistory
from .serializers import LikeHistorySerializer
from rest_framework.permissions import IsAuthenticated
from like.models import Like
class LikeHistoryListAPIView(generics.ListAPIView):
    serializer_class = LikeHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return LikeHistory.objects.filter(user=self.request.user)
        else:
            return LikeHistory.objects.none()