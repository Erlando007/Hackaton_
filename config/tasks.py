from .celery import app
from like.emails import *
from django.core.mail import send_mail

@app.task
def send_email_task(receiver_email,reciver_username):
    send_like_notification(receiver_email,reciver_username)

