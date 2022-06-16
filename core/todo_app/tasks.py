from celery import shared_task
from django.contrib.auth import get_user_model # default user model
from django.core.mail import send_mail

from core.settings import EMAIL_HOST_USER
from core.celery import app


@shared_task(bind=True)
def send_mail_func(self, email): # send mail to user
    print(f"current_email2: {email}")
    if email is not None:
        mail_subject = "Todo service"
        message = "You task status has been changed."
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email], # recipient email
            fail_silently=True, # if fails - it doesn't touch others
        )
    return "Done"
