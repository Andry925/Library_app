from django.shortcuts import redirect, render
from .models import Author


def index(request):
    authors = Author.get_all_authors()
    context = {"authors": authors}
    return render(request, "author/authors_page.html", context)


def create_new_author(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        Author.create_author(name=name, surname=surname, patronymic=patronymic)
        return redirect('author_creation_form')
    return render(request, "author/new_author.html")
