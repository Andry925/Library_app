from django.shortcuts import render
from django.views import View
from .models import Book


class AllBooksView(View):
    template_path = 'book/all_books.html'

    def get(self, request):
        all_books = Book.get_all_books()
        context = {'all_books': all_books}
        return render(request, self.template_path, context)
