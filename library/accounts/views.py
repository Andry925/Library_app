from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout


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
        return redirect("userprofile")


def logout_user(request):
    logout(request)
    return redirect("login")


def dashboard(request):
    return render(request, "accounts/userprofile.html")
