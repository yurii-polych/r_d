from django.urls import path
from .views import purchases


urlpatterns = [
    path('', purchases, name='purchase')
]
