import logging
import requests
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


logger = logging.getLogger(__name__)


# @cache_page(5 * 60)
# def say_hello(request):
#     try:
#         # send_mail('sender', 'message', settings.DEFAULT_FROM_EMAIL, ['iajmalmuhammed@gmail.com'])
#         # mail_admins('sender', 'message', html_message='<h1>hello there</h1>')
#         # message = EmailMessage('subject', 'message', settings.DEFAULT_FROM_EMAIL, ['iajmalmuhammed@gmail.com'])
#         # message.attach_file('playground/static/images/apple.jpg')
#         # message = BaseEmailMessage(
#         #     template_name='emails/hello.html',
#         #     context={'name': 'Ajmal Muhammed'}
#         # )
#         # message.send(['iajmalmuhammed@gmail.com'])
        
#         ## the below is using celery function
#         # notify_customers.delay('hello')
        
#         ##the below code is using cache with redis
#         # key = 'httpbin_result'
        
#         # if cache.get(key) is None:
#         #     response = requests.get('https://httpbin.org/delay/2')
#         #     data = response.json()
#         #     cache.set(key, data)
        
#         ## the below code shorten beacuse cache_page decorator
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Ajmal'})


## clased based view of the above function based view

class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')

        return render(request, 'hello.html', {'name': 'Ajmal'})