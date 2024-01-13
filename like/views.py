

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import LikeSerializer
from like.models import Like
from account.models import Anketa
from account.serializers import AnketaSerializer
class LikeHistoryListAPIView(generics.ListAPIView):
    serializer_class = AnketaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Like.objects.filter(user=self.request.user)
        query = Anketa.objects.none()
        for like in queryset:
            query = query.union(Anketa.objects.filter(pk=like.anketa.pk))
        return query


