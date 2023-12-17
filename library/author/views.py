from django.shortcuts import render, redirect
from django.views import View
from django.db import IntegrityError
from django.contrib import messages
from .models import Author


class AllUsersView(View):
    template_path = "author/authors_page.html"
    def get(self, request):
        all_authors = Author.get_all_authors()
        context = {"all_authors": all_authors}
        return render(request, self.template_path, context)
    
class CreateUserView(View):
    template_path = "author/new_author.html"
    redirect_url = "author_creation_form"

    def get(self,request):
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
            return render(request, "author/new_author.html")
            
