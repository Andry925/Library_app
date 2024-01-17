from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


def manage_user(user):
    if user.role == "Librarian":
        user_profile = "librarian_profile"
        return user_profile
    user_profile = "user_profile"
    return user_profile


class TestMixIn(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.role == "Librarian":
            return True
        raise PermissionDenied("You are not allowed to view this page")
