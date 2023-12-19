
def manage_user(user):
    if user.role == "Librarian":
        user_profile = "librarian_profile"
        return user_profile
    user_profile = "user_profile"
    return user_profile