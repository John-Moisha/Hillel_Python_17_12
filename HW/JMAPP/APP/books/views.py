from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
    TemplateView,
)
from books.models import Book, Author, Log


class Index(TemplateView):
    template_name = 'index.html'


# Book
class BookList(ListView):
    template_name = 'books/books_list.html'
    queryset = Book.objects.all()


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    success_url = reverse_lazy('books:book-list')
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('books:book-list')
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books:books-list')


# Authors
class AuthorList(ListView):
    template_name = 'books/authors_list.html'
    queryset = Author.objects.all()


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    success_url = reverse_lazy('books:authors-list')
    fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'native_language',
    )


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    success_url = reverse_lazy('books:authors-list')
    fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'native_language',
    )


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('books:author-list')


# log
class LogsMW(ListView):
    template_name = 'logs.html'
    queryset = Log.objects.all()
