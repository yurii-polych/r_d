from celery import shared_task

from purchase.models import Purchase
from user.models import User


@shared_task
def print_any_text():
    text = 'This function prints any text.'
    print(text)


@shared_task(bind=False)
def print_purchases_count(user_id):
    purchases_count = Purchase.objects.filter(user_id=f'{user_id}').count()
    print(purchases_count)


@shared_task
def print_user_count_every_minute():
    user_count = User.objects.all().count()
    print(user_count)
