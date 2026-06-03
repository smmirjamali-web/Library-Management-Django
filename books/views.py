from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookForm
from .forms import AuthorForm
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_create_update(request, pk=None):
    if pk is not None:
        book = get_object_or_404(Book, pk=pk)
    else:
        book = None

    if request.method == 'POST':
        if pk is not None:
            form = BookForm(request.POST, instance=book)
        else:
            form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        if pk is not None:
            form = BookForm(instance=book)
        else:
            form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:author_create')
    else:
        form = AuthorForm()

    return render(request, 'books/author_add.html', {'form': form})

        