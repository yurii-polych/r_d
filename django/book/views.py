from django.http import HttpResponse
from book.models import Book


def books(request):
    all_books = Book.objects.all().values()
    return HttpResponse(all_books)
