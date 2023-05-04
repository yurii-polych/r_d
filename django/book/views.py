from book.models import Book

from rest_framework.viewsets import ModelViewSet
from book.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.get_queryset().order_by('id')
    serializer_class = BookSerializer
    filterset_fields = ['id', 'author', ]
