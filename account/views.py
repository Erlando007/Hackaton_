
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Anketa
from .serializers import AnketaSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AnketaModelViewSet(ModelViewSet):
    queryset = Anketa.objects.all()
    serializer_class = AnketaSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response('Анкета создана',201)
        
