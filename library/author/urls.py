from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.AllAuthorsView.as_view(), name="all_authors"),
    path("add_author/", views.CreateAuthorsView.as_view(), name="author_creation_form"),
    path("edit_author/<int:pk>/",views.AuthorUpdateView.as_view(), name="edit_author"),
    path("delete_author/<int:pk>/",views.AuthorDeleteView.as_view(),name="delete_author")
]