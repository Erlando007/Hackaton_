from requests import Response
from rest_framework.generics import ListCreateAPIView
from .serializers import CommentSerializer
from .models import Comment
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwner
class StandartResultPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = StandartResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['content']
    filterset_fields = ['anketa']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


