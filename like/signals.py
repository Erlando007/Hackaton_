from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like

# @receiver(post_save, sender=Like)
# def like_post_save(sender, instance, **kwargs):
    
