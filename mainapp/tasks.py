from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    subject = 'Welcome to our Django App!'
    message = 'Thank you for registering. We are glad to have you!'
    from_email = 'your_email@example.com'  # change this to your valid email
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Welcome email sent to {email}"