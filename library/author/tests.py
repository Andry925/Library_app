from django.test import TestCase
from django.urls import reverse
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

    def test_create_authors_view_post(self):
        response = self.client.post(self.create_url, data=self.author_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "author/new_author.html")

    def test_author_update_view_post(self):
        updated_data = {
            "name": "Taras",
            "surname": "Schevchenko",
            "patronymic": "Grigorovich",
        }
        response = self.client.post(self.edit_url, data=updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("all_authors"))
