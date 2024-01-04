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
        book_form = self.book_form(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect(self.redirect_url)
        context = {"book_form": book_form}
        return render(request, self.template_path, context)


class FilteredBooksView(View):
    template_path = "book/filter_books.html"

    def get(self, request):
        author_surname = request.GET.get('author_surname')
        genre = request.GET.get('genre')
        context = {"books": self.filter_by_author(author_surname)} if author_surname else {
            "books": self.filter_by_genre(genre)}
        return render(request, self.template_path, context)

    def filter_by_author(self, author_surname):
        filtered_queryset = Book.objects.filter(
            author__surname__iexact=author_surname)
        return filtered_queryset

    def filter_by_genre(self, genre):
        pass



