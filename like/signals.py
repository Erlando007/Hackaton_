from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Like
from account.models import Anketa
from .emails import send_like_notification,send_like_deleted,send_like_notification_vs

@receiver(post_save, sender=Like)
def like_anket_save(sender, instance, created, **kwargs):
    if created:
        sender_username = instance.user.username
        receiver_username =  instance.anketa.user.username
        receiver_email = instance.anketa.user.email  
        liked_user= instance.anketa.user
        like_sender = Anketa.objects.filter(user=instance.user).first().user
        anket_sender = Anketa.objects.filter(user=instance.user).first()
        if Like.objects.filter(user = liked_user,anketa = anket_sender).exists():
            send_like_notification_vs(like_sender,liked_user)
        else:
            send_like_notification(receiver_username, receiver_email,sender_username)

# def like_notification(sender, instance, created, **kwargs):
#     if created:
#         user1 = instance.user
#         user2 = Anketa.objects.get(id=instance.anketa.id).user

#         Проверяем, есть ли взаимный лайк
#         if Like.objects.filter(user=user2, anketa=instance.anketa).exists():
#             send_like_notification(user1, user2)
#             send_like_notification(user2, user1)

# @receiver(post_delete, sender=Like)
# def like_post_delete(sender, instance, **kwargs):
#     sender_username = instance.user.username
#     receiver_username =  instance.anketa.user.username

#     receiver_email = instance.user.email  
#     send_like_deleted(sender_username, receiver_email,receiver_username)