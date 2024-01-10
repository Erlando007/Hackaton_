
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Anketa
from .serializers import AnketaSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import action
from like.models import Like


class AnketaModelViewSet(ModelViewSet):
    queryset = Anketa.objects.all()
    serializer_class = AnketaSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response('Анкета создана',201)
    
    @action(detail=True, methods=['POST'])
    def toggle_like(self, request, pk=None):
        anketa = self.get_object()
        like = request.user.like.filter(anketa = anketa)
        if like:
            like.delete()
            return Response(f'Вы убрали лайк с анкеты {anketa.first_name}', 204)
        like = Like.objects.create(
            anketa=anketa,
            user=request.user
        )
        return Response(f'Вы лайкнули анкету {anketa.first_name}', 201)
