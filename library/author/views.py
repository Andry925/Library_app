from django.shortcuts import render
from .models import Author

# Create your views here.

def index(request):
    authors = Author.get_all_authors()
    context = {"authors":authors}
    return render(request,"author/authors_page.html",context)


