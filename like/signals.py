from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Like
from account.models import Anketa
from config.tasks import send_email_task1,send_email_task2,send_email_task3

@receiver(post_save, sender=Like)
def like_anket_save(sender, instance, created, **kwargs):
    if created: 
        instance.anketa.likes_count += 1
        instance.anketa.save()
        sender_username = instance.user.username
        receiver_email = instance.anketa.user.email  
        liked_user= instance.anketa.user
        like_sender = Anketa.objects.filter(user=instance.user.pk).first() 
        anket_sender = Anketa.objects.filter(user=instance.user.pk).first()
        if Like.objects.filter(user = liked_user,anketa = anket_sender).exists():
            send_email_task2.delay(like_sender.user.email,liked_user.email)
        else:
            send_email_task1.delay(receiver_email,sender_username)


@receiver(post_delete, sender=Like)
def like_post_delete(sender, instance, **kwargs):
    receiver_username =  instance.anketa.user
    instance.anketa.likes_count -= 1
    instance.anketa.save()
    receiver_email = instance.user.email  
    send_email_task3.delay(receiver_username.email, receiver_email)