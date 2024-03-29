from .models import Anketa
from rest_framework import serializers

class AnketaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Anketa
        fields = ['first_name', 'last_name', 'sex', 'zodiac','age','likes_count','height','photo']
    
    
    def create(self,validated_data):
        request = self.context.get('request')
        user = request.user
        if Anketa.objects.filter(user=user).exists():
            raise serializers.ValidationError('У этого пользователя уже есть анкета')
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
    


    