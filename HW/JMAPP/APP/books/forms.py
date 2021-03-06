from django import forms

from books.models import Book
from books.models import Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'author',
            'title',
            'publish_year',
            'review',
            'condition',
        )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
            'date_of_birth',
            'date_of_death',
            'country',
            'gender',
            'native_language',
        )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
