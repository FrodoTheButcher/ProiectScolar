from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

@shared_task
def send_account_created_email(username, email):
    subject = 'Contul tau a fost creat!'
    message = 'Salut, %s! Contul tau a fost creat cu succes.' % username
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
