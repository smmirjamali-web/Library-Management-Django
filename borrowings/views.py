from django.shortcuts import render

# Create your views here.
def borrow(request):
    return render(request, 'borrowings/borrow.html')