from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Author


class AuthorViewsTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'Andrew',
            'last_name': 'some',
            'username': 'andrew',
            'role': 'Librarian',
        }
        self.author_data = {
            "name": "Mykola",
            "surname": "Hohol",
            "patronymic": "Vasiliovich",
        }
        self.author = Author.objects.create(**self.author_data)
        self.user_librarian = get_user_model().objects.create(**self.user_data)
        self.client.force_login(self.user_librarian)

    def test_author_page_for_logged_in_user(self):
        response = self.client.get(reverse('all_authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/authors_page.html')

    def test_author_page_for_not_logged_out_users(self):
        self.client.logout()
        response = self.client.get(reverse('all_authors'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/librarian_profile/authors/")