from book.models import Book
from book.forms import BookCreateForm

from django.views.generic import ListView, CreateView, DetailView


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    success_url = '/books'
