
from .celery import app
from like.emails import *
from django.core.mail import send_mail

@app.task
def send_email_task1(receiver_email,reciver_username):
    send_like_notification(receiver_email,reciver_username)

@app.task
def send_email_task2(receiver_email,reciver_username):
    send_like_notification_vs(receiver_email,reciver_username)

@app.task
def send_email_task3(receiver_email,reciver_username):
    send_like_deleted(receiver_email,reciver_username)


