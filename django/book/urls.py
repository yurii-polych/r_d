from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView


urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('create', BookCreateView.as_view(), name='book-create'),
]
