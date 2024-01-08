from django.db import models

# Create your models here.

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
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=20, choices=SEX)
    zodiac = models.CharField(max_length=20, choices=ZODIAC)