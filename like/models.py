from django.db import models
from account.models import Anketa

# Create your models here.

class Like(models.Model):
    anketa = models.ForeignKey(
        Anketa,
        related_name='likes',
        on_delete=models.CASCADE
    )


