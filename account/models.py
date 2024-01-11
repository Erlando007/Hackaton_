from django.db import models
# Create your models here.
from django.contrib.auth.models import User
class Anketa(models.Model):
    SEX = (
        ('male', 'Мужчина'),
        ('female', 'Женщина'),
        ('think', 'Неопределенный')
    )
    ZODIAC = (
        ('Aries', 'Овен'),
        ('Taurus', 'Телец'),
        ('Gemini', 'Близнецы'),
        ('Cancer', 'Рак'),
        ('Leo', 'Лев'),
        ('Virgo', 'Дева'),
        ('Libra', 'Весы'),
        ('Scorpio', 'Скорпион'),
        ('Sagittarius', 'Стрелец'),
        ('Capricorn', 'Козерог'),
        ('Aquarius', 'Водолей'),
        ('Pisces', 'Рыбы')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null = True)
    created_at = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/')
    age = models.IntegerField(default = 18)
    sex = models.CharField(max_length=20, choices=SEX)
    zodiac = models.CharField(max_length=20, choices=ZODIAC)
    height = models.IntegerField(default = 170)
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE,
        related_name='anket')   

    def __str__(self):
        return f'first_name: {self.first_name} anket: {self.user}'