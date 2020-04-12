import time
from datetime import timedelta

from celery.schedules import crontab
from django.contrib.auth.models import User
from django.core.mail import send_mail
from shop.models import Product
from amaizing_shop import settings

@shared_task
def hard_logic():
    time.sleep(5)
    return "It works!"

def mailing_list():
    user_emails = dict(User.objects.exclude(email='')).values_list('username', 'email')
    return user_emails


def new_products():
    products = Product.objects.filter(
        created_at__gte=timezone.now() - timedelta(
            days=settings.NEW_PRODUCT_DAYS)
    )
    list_products = [f'{product.title}: {product.price}$' for product in
                     products]
    return '\n'.join(list_products)

@shared_task
def my_periodic_logic():
    print('Run logic!!')


SCHEDULE = {
    'my_periodic_logic': {
        'task': 'shop.tasks.my_periodic_logic',
        'args': (),
        'options': {},
        'schedule': timedelta(seconds=5)
    },
    'send_email_task': {
        'task': 'shop.tasks.send_email_task',
        'args': (),
        'options': {},
        'schedule': crontab(minute='30', hour='9', day_of_week='mon')
    }
}

@shared_task
def send_email_task():
    products = new_products()
    users = mailing_list()
    send_mail(
        'New products',
        f'HelloThe list of new products:',
        'amazing.shop.test@gmail.com',
        ['mrtwister5950@mail.com']
    )