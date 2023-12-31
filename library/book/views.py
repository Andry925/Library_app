from django.shortcuts import render
from django.views import View
from .models import Book
from .forms import BookCreationForm


class AllBooksView(View):
    template_path = "book/all_books.html"

    def get(self, request):
        all_books = Book.get_all_books()
        context = {"all_books": all_books}
        return render(request, self.template_path, context)


class AddBookView(View):
    template_path = "book/add_new_book.html"
    book_form = BookCreationForm

    def get(self, request):
        book_creation_form = self.book_form()
        context = {"book_form": book_creation_form}
        return render(request, self.template_path, context)
