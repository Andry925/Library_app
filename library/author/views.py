from django.shortcuts import render
from django.views import View
from .models import Author


class AllUsers(View):
    template_path = "author/authors_page.html"
    redirect_url = "author_creation_form"

    def get(self, request):
        all_users = Author.get_all_authors()
        context = {"all_users", all_users}
        return render(request, self.template_path, context)
