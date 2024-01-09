from .models import Anketa
from rest_framework import serializers

class AnketaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Anketa
        fields = ['first_name', 'last_name', 'sex', 'zodiac', 'user','age']
    
    
    def create(self,validated_data):
        validated_data['first_name'] = validated_data.get('first_name').capitalize()
        validated_data['last_name'] = validated_data.get('last_name').capitalize()
        return super().create(validated_data)
    def validate_age(self,age):
        if age < 18:
            raise serializers.ValidationError('Ваш возраст не соответствует условиям политики сайта')
    
    
    
    # def create(self, validated_data):
    #     anket = Anketa.objects.create(**validated_data)
    #     anket
    #     anket.save()
    #     return user
    