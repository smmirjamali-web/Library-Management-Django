from django import forms

from . models import Book, Author, Category

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'category', 'total_copies']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'age']
