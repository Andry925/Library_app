from django.shortcuts import render, redirect
from django.views import View
from django.db import IntegrityError
from django.contrib import messages
from .models import Author


class AllAuthorsView(View):
    template_path = "author/authors_page.html"

    def get(self, request):
        all_authors = Author.get_all_authors()
        context = {"all_authors": all_authors}
        return render(request, self.template_path, context)


class CreateAuthorsView(View):
    template_path = "author/new_author.html"
    redirect_url = "author_creation_form"

    def get(self, request):
        return render(request, self.template_path)

    def post(self, request):
        try:
            Author.create_author(
                name=request.POST.get('name'),
                surname=request.POST.get('surname'),
                patronymic=request.POST.get('patronymic'))
            return redirect(self.redirect_url)
        except IntegrityError:
            error_message = "Author with this surname already exists"
            messages.error(request, error_message)
            return render(request, self.template_path)


class AuthorUpdateView(View):
    template_path = "author/edit_author.html"
    redirect_url = "all_authors"
    fields = ("name", "surname", "patronymic")

    def get(self, request, pk):
        author = Author.get_author_by_id(pk=pk)
        field_values = {field: getattr(author, field) for field in self.fields}
        self.context = {"author": author, "field_values": field_values}
        return render(request, self.template_path, self.context)

    def post(self, request, pk):
        author = Author.get_author_by_id(pk=pk)
        for field in self.fields:
            setattr(author, field, request.POST.get(field))
        try:
            author.save()
        except IntegrityError:
            error_message = "Author with this surname already exists"
            messages.error(request, error_message)
            self.get(request, pk)
            return render(request, self.template_path, self.context)
        return redirect(self.redirect_url)


class AuthorDeleteView(View):
    redirect_url = "all_authors"

    def get(self, request, pk):
        Author.delete_by_id(pk=pk)
        return redirect(self.redirect_url)
