from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . utils import manage_user
from .forms import UserForm


def registration(request):
    if request.method != "POST":
        user_form = UserForm()
        context = {
            "user_form": user_form
        }
        return render(request, "accounts/register.html", context)
    user_form_with_data = UserForm(request.POST)

    if not user_form_with_data.is_valid():
        context = {
            "user_form": user_form_with_data}
        return render(request, "accounts/register.html", context)
    object_with_hashed_password = hash_password(user_form=user_form_with_data)
    object_with_hashed_password.save()
    return redirect("register")


def hash_password(user_form):
    password = user_form.cleaned_data["password"]
    user = user_form.save(commit=False)
    user.set_password(password)
    return user


def login_user(request):
    if request.method != "POST":
        return render(request, "accounts/login.html")

    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(email=email, password=password)
    if user:
        login(request, user)
        return determine_appropraite_profile(request)


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def determine_appropraite_profile(request):
    user = request.user
    user_url = manage_user(user)
    return redirect(user_url)


@login_required(login_url="login")
def redirect_user(request):
    return render(request, "accounts/userprofile.html")


@login_required(login_url="login")
def redirect_librarian(request):
    return render(request, "accounts/librarianprofile.html")
