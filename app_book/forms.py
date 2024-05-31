# book_hub/users/forms.py
from django import forms
from .models import CustomUser,Book
from django import forms

class CustomUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']  # Add other fields as needed
# book_hub/catalog/forms.py

class Book(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn']  # Add book fields as needed
