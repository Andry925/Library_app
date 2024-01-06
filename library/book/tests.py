from django.test import TestCase
from django.urls import reverse
from django.db import IntegrityError, transaction
from .models import Book
from author.models import Author
from .forms import BookCreationForm


class BookTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Mykola", surname="Hohol", patronymic="Vasiliovich")
        self.data = {
            'name': 'Test Book',
            'count': 2,
            'genre': 'roman',
            'author': self.author.pk}

    def test_all_books_view(self):
        response = self.client.get(reverse('all_books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/all_books.html')

    def test_add_book_get(self):
        response = self.client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/add_new_book.html')
        self.assertIsInstance(response.context['book_form'], BookCreationForm)

    def test_add_book_view_post_valid_form(self):
        response = self.client.post(reverse('add_book'), self.data)
        self.assertTrue(Book.objects.filter(name='Test Book').exists())
