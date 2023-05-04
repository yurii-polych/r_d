from book.models import Book

from rest_framework.viewsets import ModelViewSet
from book.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
