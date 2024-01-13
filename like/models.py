from django.db import models
from account.models import Anketa
from django.contrib.auth.models import User

# Create your models here.

class Like(models.Model):
    user = models.ForeignKey(
        'auth.User', 
        related_name='like',
        on_delete=models.CASCADE,
    )
    anketa = models.ForeignKey(
        Anketa,
        related_name='like',
        on_delete=models.CASCADE
    )


class LikeHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_user')
    liked_by = models.ForeignKey(Anketa, on_delete=models.CASCADE, related_name='liked_by_user')
    timestamp = models.DateTimeField(auto_now_add=True)

