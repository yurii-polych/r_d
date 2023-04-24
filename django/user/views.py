from django.http import HttpResponse
from user.models import User


def users(request):
    all_users = User.objects.all().values()
    return HttpResponse(all_users)
