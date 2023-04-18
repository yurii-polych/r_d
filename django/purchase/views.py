from django.http import HttpResponse
from .models import Purchase


def purchases(request):
    all_purchases = Purchase.objects.all().values()
    return HttpResponse(all_purchases)
