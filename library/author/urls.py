from django.urls import path
from . import views

urlpatterns = [
    path("authors/",views.index,name="all_authors"),
    path("add_author/",views.create_new_author, name="author_creation_form"),
]