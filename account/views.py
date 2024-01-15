from rest_framework.viewsets import ModelViewSet
from .models import Anketa
from .serializers import AnketaSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from like.models import Like
from comment.serializers import CommentSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import default_storage
from rest_framework.generics import ListAPIView


class AnketaModelViewSet(ModelViewSet):
    queryset = Anketa.objects.all()
    serializer_class = AnketaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
        
        return Response(f'Вы лайкнули анкету ', 201)
    
    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        anket = self.get_object()
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(anketa=anket)
        return Response('успешно добавлено', 201)
    
    def retrieve(self, request, *args, **kwargs):
        anket = self.get_object()
        instagram_username = anket.instagram_username
        serializer = AnketaSerializer(instance=anket)
        serialized_data = serializer.data
        comment_serializer = CommentSerializer(instance=anket.comments, many=True)
        serialized_data['comments'] = comment_serializer.data
        serialized_data['instagram_username'] = instagram_username
        return Response(serialized_data)
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            return super().update(request, *args, **kwargs)
        return Response('Вы не можете отредактировать чужую анкету')
        
    

class ImageDetailView(APIView):
    def get(self, request, pk):
        anketa = get_object_or_404(Anketa, pk=pk)
        image_path = anketa.photo.path

        if not default_storage.exists(image_path):
            return Response({'detail': 'Файл не найден'}, status=status.HTTP_404_NOT_FOUND)
        
        with default_storage.open(image_path, 'rb') as image_file:
            response = HttpResponse(image_file.read(), content_type='image/jpeg')
            response['Content-Disposition'] = f'inline; filename="{anketa.photo.name}"'
            return response

class RatingListAPIView(ListAPIView):
    queryset = Anketa.objects.all()
    serializer_class = AnketaSerializer

    def get_queryset(self):
        queryset = Anketa.objects.all().order_by('-likes_count')
        return queryset






