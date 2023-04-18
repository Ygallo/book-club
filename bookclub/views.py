from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.order_by('title')
    template_name = 'books.html'
    paginate_by = 8
