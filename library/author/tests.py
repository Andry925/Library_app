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
        self.edit_url = reverse("edit_author", args=[self.author.pk])
        self.delete_url = reverse("delete_author", args=[self.author.pk])
        self.user_librarian = get_user_model().objects.create(**self.user_data)
        self.user_data['username'] = 'John'
        self.user_data['role'] = 'User'
        self.user_data['email'] = 'some@gmail.com'
        self.user_user = get_user_model().objects.create(**self.user_data)
        self.client.force_login(self.user_librarian)

    def test_author_page_for_logged_in_user(self):
        response = self.client.get(reverse('all_authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/authors_page.html')

    def test_author_page_for_logged_out_users(self):
        self.client.logout()
        response = self.client.get(reverse('all_authors'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/librarian_profile/authors/")

    def test_author_for_non_authorized_user(self):
        self.client.force_login(self.user_user)
        response = self.client.get(reverse('all_authors'))
        self.assertEqual(response.status_code, 403)

    def test_create_author_view_get(self):
        response = self.client.get(reverse('author_creation_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/new_author.html')

    def test_create_author_view_post(self):
        new_author_data = {
            "name": "Taras",
            "surname": "Schevchenko",
            "patronymic": "Grigorovich"
        }
        response = self.client.post(reverse('author_creation_form'), data=new_author_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/librarian_profile/authors/")

    def test_create_author_view_duplicate(self):
        response = self.client.post(reverse('author_creation_form'), data=self.author_data)
        self.assertContains(response, "<strong>Author with this surname already exists</strong>", status_code=200)
        self.assertTemplateUsed(response, 'author/new_author.html')

    def test_update_author_view_get(self):
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/edit_author.html')

    def test_update_author_view_post(self):
        self.author_data['name'] = 'Mykola'
        response = self.client.post(self.edit_url, data=self.author_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/librarian_profile/authors/")

    def test_delete_author_view_get(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/librarian_profile/authors/")
