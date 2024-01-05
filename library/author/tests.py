from django.test import TestCase
from django.urls import reverse
from django.db import IntegrityError, transaction
from .models import Author


class AuthorViewsTestCase(TestCase):
    def setUp(self):
        self.author_data = {
            "name": "Mykola",
            "surname": "Hohol",
            "patronymic": "Vasiliovich",
        }
        self.author = Author.objects.create(**self.author_data)
        self.create_url = reverse("author_creation_form")
        self.edit_url = reverse("edit_author", args=[self.author.pk])
        self.delete_url = reverse("delete_author", args=[self.author.pk])

    def test_all_authors_view(self):
        response = self.client.get(reverse("all_authors"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "author/authors_page.html")

    def test_create_authors_view_get(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "author/new_author.html")
