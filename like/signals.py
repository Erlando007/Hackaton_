from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Like
from account.models import Anketa
from .emails import send_like_notification,send_like_deleted,send_like_notification_vs

@receiver(post_save, sender=Like)
def like_anket_save(sender, instance, created, **kwargs):
    if created:
        sender_username = instance.user.username
        receiver_email = instance.user.email  
        user1 = instance.user
        user2 = Anketa.objects.get(id=instance.anketa.id).user
        if Like.objects.filter(user=user2, anketa=instance.anketa).exists():
            send_like_notification_vs(user1, user2)
            send_like_notification_vs(user2, user1)
        else:
            send_like_notification(sender_username, receiver_email)

# def like_notification(sender, instance, created, **kwargs):
#     if created:
#         user1 = instance.user
#         user2 = Anketa.objects.get(id=instance.anketa.id).user

#         Проверяем, есть ли взаимный лайк
#         if Like.objects.filter(user=user2, anketa=instance.anketa).exists():
#             send_like_notification(user1, user2)
#             send_like_notification(user2, user1)

@receiver(post_delete, sender=Like)
def like_post_delete(sender, instance, **kwargs):
    sender_username = instance.user.username
    receiver_email = instance.user.email  
    send_like_deleted(sender_username, receiver_email)