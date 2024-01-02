from django.shortcuts import redirect, render
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
    redirect_url = "all_books"

    def get(self, request):
        book_creation_form = self.book_form()
        context = {"book_form": book_creation_form}
        return render(request, self.template_path, context)

    def post(self, request):
        create_user_form = self.book_form(request.POST)
        if create_user_form.is_valid():
            create_user_form.save()
            return redirect(self.redirect_url)
        context = {"book_form": create_user_form}
        return render(request, self.template_path, context)
