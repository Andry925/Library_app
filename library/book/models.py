from django.db import models
from author.models import Author


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    count = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=10, blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books")

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def get_book_details(pk):
        try:
            book = Book.objects.get(pk=pk)

        except Book.DoesNotExist:
            return None
        return book

    @staticmethod
    def get_all_books():
        return Book.objects.all().order_by("id")

    @staticmethod
    def delete_book(pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return True

        except Book.DoesNotExist:
            return False
