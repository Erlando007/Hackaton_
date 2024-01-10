from django.core.mail import send_mail

def send_like_notification(sender_username, receiver_email):
    subject = 'Новый лайк'
    message = f'Пользователь {sender_username} поставил вам лайк!'
    from_email = 'Ascar6000@gmail.com'
    recipient_list = [receiver_email]
    send_mail(subject, message, from_email, recipient_list)

def send_like_notification_vs(user1, user2):
    subject = 'Взаимный лайк'
    message = f'У вас с {user1.username} Взаимные лайки!'
    from_email = 'Ascar6000@gmail.com'  
    recipient_list = [user1.email, user2.email]

    send_mail(subject, message, from_email, recipient_list)


def send_like_deleted(sender_username, receiver_email):
    subject = 'Вы потеряли один лайк'
    message = f'Пользователь {sender_username} убрал лайк из вашей анкеты, сделайте с этим что нибудь!'
    from_email = 'Ascar6000@gmail.com'
    recipient_list = [receiver_email]
    send_mail(subject, message, from_email, recipient_list)
