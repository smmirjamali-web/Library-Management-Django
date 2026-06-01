from django.shortcuts import render

# Create your views here.

def book_list(request):
    return render(request, 'books/book_list.html')

def book_detail(request, pk):
    return render(request, 'books/book_detail.html')

def book_create_update(request, pk):
    return render(request, 'books/book_create_update.html')
