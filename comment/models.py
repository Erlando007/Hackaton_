from django.db import models
from account.models import Anketa

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    anketa = models.ForeignKey(
        Anketa, 
        on_delete=models.CASCADE,
        related_name='comments'
    )