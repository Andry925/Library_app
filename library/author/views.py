from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import IntegrityError
from django.contrib import messages
from accounts.utils import TestMixIn
from .models import Author


@method_decorator(login_required(login_url="login"), name="dispatch")
class AllAuthorsView(TestMixIn, View):
    template_path = "author/authors_page.html"

    def get(self, request):
        all_authors = Author.get_all_authors()
        user = self.request.user
        context = {"all_authors": all_authors, "user": user}
        return render(request, self.template_path, context)


@method_decorator(login_required(login_url="login"), name="dispatch")
class CreateAuthorsView(TestMixIn, View):
    template_path = "author/new_author.html"
    redirect_url = "all_authors"

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


@method_decorator(login_required(login_url="login"), name="dispatch")
class AuthorUpdateView(TestMixIn, View):
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
            error_message = "Not a valid surname to change"
            messages.error(request, error_message)
            self.get(request, pk)
            return render(request, self.template_path, self.context)
        return redirect(self.redirect_url)


@method_decorator(login_required(login_url="login"), name="dispatch")
class AuthorDeleteView(TestMixIn, View):
    redirect_url = "all_authors"

    def get(self, request, pk):
        Author.delete_by_id(pk=pk)
        return redirect(self.redirect_url)
