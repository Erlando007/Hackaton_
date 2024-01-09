from django.db import models

# Create your models here.

class Recomendation(models.Model):
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
    min_age = models.IntegerField(default = 18)
    max_age = models.IntegerField(default = 50)
    sex = models.CharField(max_length=20, choices=SEX)
    zodiac = models.CharField(max_length=20, choices=ZODIAC, null = True)
    user = models.ForeignKey('auth.User', 
        on_delete=models.CASCADE,
        related_name='rekomendations')