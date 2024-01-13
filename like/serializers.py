from rest_framework import serializers
from like.models import Like

class LikeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'