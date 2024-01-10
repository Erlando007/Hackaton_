from .models import Anketa
from rest_framework import serializers
from comment.serializers import CommentSerializer
class AnketaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    comments = serializers.SerializerMethodField(method_name='get_comments')
    likes_count = serializers.SerializerMethodField(method_name='get_likes_count')
    class Meta:
        model = Anketa
        fields = ['first_name', 'last_name', 'sex', 'zodiac', 'user','age','comments','likes_count']
    
    def get_likes_count(self, instance):
        likes_counter = instance.like.all().count()
        return likes_counter
    def get_comments(self, instance):
        comments = instance.comments.all()
        serializer = CommentSerializer(
            comments, many=True
        )
        return serializer.data
    
    def create(self,validated_data):
        validated_data['first_name'] = validated_data.get('first_name').capitalize()
        validated_data['last_name'] = validated_data.get('last_name').capitalize()
        anket = Anketa.objects.create(**validated_data)
        anket.save()
        return anket
    
    def validate_age(self,age):
        if age <= 18:
            raise serializers.ValidationError('Ваш возраст не соответствует условиям политики сайта')
        return age
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = instance.id
        return repr
    

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     children = instance.children.all()
    #     if children:
    #         repr['children'] = CategorySerializer(
    #             children, many=True
    #         ).data
    #     repr['makers'] = 'makers'
    #     return repr
    
    
    # def create(self, validated_data):
    #     anket = Anketa.objects.create(**validated_data)
    #     anket
    #     anket.save()
    #     return user
    