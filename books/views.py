from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookForm
# Create your views here.

def book_list(request):
    return render(request, 'books/book_list.html')

def book_detail(request, pk):
    return render(request, 'books/book_detail.html')

def book_create_update(request, pk=None):
    if pk is not None:
        book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        if pk is not None:
            form = BookForm(request.POST, instance=book)
        else:
            form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('books:book_list')


        