from django.db import models
from account.models import Anketa

# Create your models here.

class Like(models.Model):
    user = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
        related_name='like'
    )
    anketa = models.ForeignKey(
        Anketa,
        related_name='like',
        on_delete=models.CASCADE
    )
    