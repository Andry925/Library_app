from django import forms
from .models import Book


class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name","count","genre","author"]
