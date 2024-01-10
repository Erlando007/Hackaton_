
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Anketa
from .serializers import AnketaSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import action
from like.models import Like
from comment.serializers import CommentSerializer

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
    
    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post, owner=request.user)
        return Response('успешно добавлено', 201)
    # def retrieve(self, request, *args, **kwargs):
    #     anket = self.get_object()
    #     comments = anket.comments.all()
    #     serializer = CommentSerializer(comments, many=True)
    #     return Response(serializer.data)
    # @action(detail=True, methods=['GET'])
    # def comment(self,request,pk=None):
    #     anket = self.get_object()
    #     print(anket)
    #     comments = anket.comments.all()
    #     serializer = CommentSerializer(comments, many=True)
    #     return Response(serializer.data)
