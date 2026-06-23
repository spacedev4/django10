from django.shortcuts import render
from .models import Author
from .models import Genre
from .models import Book
from django.http import HttpResponse

def author_list(requests):
    authors = Author.objects.all()
    authors_list = ""
    for author in authors:
        authors_list += f"<li>{author.name}</li>"
    return HttpResponse(f"<ul>{authors_list}</ul>")

def genre_list(requests):
    genres = Genre.objects.all()
    genres_list = ""
    for genre in genres:
        genres_list += f"<li>{genre.name}</li>"
    return HttpResponse(f"<ul>{genres_list}</ul>")

def book_list(requests):
    books = Book.objects.all()
    books_list = ""
    for book in books:
        books_list += f"<li>{book.name}</li>"
    return HttpResponse(f"<ul>{books_list}</ul>")


def alls(request):
    authors_list = "".join([f"<li>{a.name}</li>" for a in Author.objects.all()])
    genres_list = "".join([f"<li>{g.name}</li>" for g in Genre.objects.all()])
    books_list = "".join([f"<li>{b.name}</li>" for b in Book.objects.all()])
    return HttpResponse(
        f"<h2>Authors</h2><ul>{authors_list}</ul>"
        f"<h2>Genres</h2><ul>{genres_list}</ul>"
        f"<h2>Books</h2><ul>{books_list}</ul>"
    )