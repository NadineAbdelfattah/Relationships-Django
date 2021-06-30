from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg


# Create your views here.
def index(request):
    books = Book.objects.all()
    books_num = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "index.html", {
        "books": books,
        "books_num": books_num,
        "avg_rating": avg_rating
    })


def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, "book_detail.html", {
        "title": book.title,
        "rating": book.rating,
        "author": book.author,
        "is_bestselling": book.is_bestselling
    })
