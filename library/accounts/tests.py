from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AccountTests(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'Andrew',
            'last_name': 'some',
            'username': 'johndoe',
            'role': 'User',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)

    def test_user_profile_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/userprofile.html')

    def test_librarian_profile_view(self):
        librarian_data = {
            'email': 'librarian@example.com',
            'password': 'librarianpassword',
            'first_name': 'Librarian',
            'last_name': 'User',
            'username': 'librarian',
            'role': 'Librarian',
        }
        librarian = get_user_model().objects.create_user(**librarian_data)
        self.client.force_login(librarian)
        response = self.client.get(reverse('librarian_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/librarianprofile.html')

    def test_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
