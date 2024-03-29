from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.utils import TestMixIn
from .models import Book
from .forms import BookCreationForm, BookEditForm


@method_decorator(login_required(login_url="login"), name="dispatch")
class AllBooksView(TestMixIn,View):
    template_path = "book/all_books.html"

    def get(self, request):
        all_books = Book.get_all_books()
        context = {"all_books": all_books}
        return render(request, self.template_path, context)


@method_decorator(login_required(login_url="login"), name="dispatch")
class AddBookView(TestMixIn,View):
    template_path = "book/add_new_book.html"
    book_form = BookCreationForm
    redirect_url = "all_books"

    def get(self, request):
        book_creation_form = self.book_form()
        context = {"book_form": book_creation_form}
        return render(request, self.template_path, context)

    def post(self, request):
        book_form = self.book_form(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect(self.redirect_url)
        context = {"book_form": book_form}
        return render(request, self.template_path, context)


@method_decorator(login_required(login_url="login"), name="dispatch")
class FilteredBooksView(TestMixIn,View):
    template_path = "book/filter_books.html"

    def get(self, request):
        author_surname = request.GET.get('author_surname')
        genre = request.GET.get('genre')
        context = {"books": self.filter_by_author(author_surname)} if author_surname else {
            "books": self.filter_by_genre(genre)}
        return render(request, self.template_path, context)

    def filter_by_author(self, author_surname):
        filtered_queryset = Book.objects.filter(
            author__surname__iexact=author_surname).order_by("id")
        return filtered_queryset

    def filter_by_genre(self, genre):
        filtered_queryset = Book.objects.filter(genre=genre).order_by("id")
        return filtered_queryset


@method_decorator(login_required(login_url="login"), name="dispatch")
class EditBookView(TestMixIn,View):
    template_path = "book/edit_book.html"
    redirect_url = "all_books"
    edit_form = BookEditForm

    def get(self, request, pk):
        book_instance = Book.get_book_details(pk=pk)
        edit_book = self.edit_form()
        context = {"book": book_instance,
                   "edit_book_form": edit_book}
        return render(request, self.template_path, context)

    def post(self, request, pk):
        book_instance = Book.get_book_details(pk=pk)
        edit_book_to_save = self.edit_form(
            request.POST, instance=book_instance)
        if edit_book_to_save.is_valid():
            edit_book_to_save.save()
            return redirect(self.redirect_url)
        context = {"book": book_instance}
        return render(request, self.template_path, context)


@method_decorator(login_required(login_url="login"), name="dispatch")
class DeleteBookView(TestMixIn,View):

    redirect_url = "all_books"

    def get(self, request, pk):
        book = Book.get_book_details(pk=pk)
        book.delete()
        return redirect(self.redirect_url)
