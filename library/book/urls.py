from django.urls import path
from . import views

urlpatterns = [
    path("all_books/", views.AllBooksView.as_view(), name="all_books")

]
