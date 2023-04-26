from django import forms
from book.models import Book


class BookCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    author = forms.CharField(widget=forms.TextInput)
    year = forms.CharField(widget=forms.NumberInput)
    price = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'price')
