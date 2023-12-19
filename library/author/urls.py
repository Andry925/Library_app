from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.AllUsersView.as_view(), name="all_authors"),
    path("add_author/", views.CreateUserView.as_view(), name="author_creation_form"),
]