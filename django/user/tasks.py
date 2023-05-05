from celery import shared_task


@shared_task
def print_any_text():
    text = 'This function prints any text.'
    print(text)
