from celery import shared_task
from templated_mail.mail import BaseEmailMessage
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage


@shared_task
def notify_customers(messages):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={
                'name': 'Ajmal Muhammed',
                'message': messages
            }
        )
        message.send(['iajmalmuhammed@gmail.com'])
        print("Email sent successfully")
    except BadHeaderError:
        pass