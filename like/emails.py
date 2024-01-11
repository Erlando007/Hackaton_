from django.core.mail import send_mail

def send_like_notification(receiver_email,reciver_username):
    subject = 'Новый лайк'
    message = f'Пользователь {reciver_username} поставил вам лайк!'
    from_email = 'Ascar6000@gmail.com'
    recipient_list = [receiver_email]
    send_mail(subject, message, from_email, recipient_list)

def send_like_notification_vs(user1, user2):
    subject = 'Взаимный лайк'
    message1 = f'У вас с {user2.username} Взаимные лайки!'
    message2 = f'У вас с {user1.username} Взаимные лайки!'
    from_email = 'Ascar6000@gmail.com'

    recipient_list1 = [user1.email]
    recipient_list2 = [user2.email]

    send_mail(subject, message1, from_email, recipient_list1)
    send_mail(subject, message2, from_email, recipient_list2)
    

def send_like_deleted(receiver_email,receiver_username):
    subject = 'Вы потеряли один лайк'
    message = f'Пользователь {receiver_username} убрал лайк из вашей анкеты, сделайте с этим что нибудь!'
    from_email = 'Ascar6000@gmail.com'
    recipient_list = [receiver_email]
    send_mail(subject, message, from_email, recipient_list)
