from django.contrib import admin
from .models import Purchase


@admin.register(Purchase)
class Purchase(admin.ModelAdmin):
    list_display = ('user', 'book', 'date')
