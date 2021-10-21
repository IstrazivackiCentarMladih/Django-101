from django.shortcuts import render, redirect
from .models import Book
from .form import BookForm
from django.http import Http404, HttpRequest


def create(request: HttpRequest):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

    return render(request, 'books/create.html', {'create_form': BookForm()})


def delete(request: HttpRequest, book_id: str):
    try:
        book = Book.objects.get(pk=book_id).delete()
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return redirect('index')


def detail(request: HttpRequest, book_id: str):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'books/detail.html', {'book': book})


def index(request: HttpRequest):
    book_list = Book.objects.order_by('-pub_year')
    context = {'books_list': book_list}
    return render(request, 'books/index.html', context)
