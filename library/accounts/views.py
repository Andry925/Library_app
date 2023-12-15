from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .utils import manage_user
from .forms import UserForm


class RegistrationView(View):
    template_name = "accounts/register.html"
    user_form = UserForm

    def get(self, request):
        registration_form = self.user_form()
        context = {"registration_form": registration_form}
        return render(request, self.template_name, context)

    def post(self, request):
        registration_form = self.user_form(request.POST)
        if registration_form.is_valid():
            user_with_hashed_password = self.hash_password(registration_form)
            user_with_hashed_password.save()
            return redirect("login")
        context = {"registration_form": registration_form}
        return render(request, self.template_name, context)

    def hash_password(self, valid_user_form):
        password = valid_user_form.cleaned_data.get("password")
        user = valid_user_form.save(commit=False)
        user.set_password(password)
        return user


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return self.determine_appropriate_profile(request)
        return render(request, self.template_name)

    def determine_appropriate_profile(self, request):
        user = request.user
        user_url = manage_user(user)
        return redirect(user_url)


@method_decorator(login_required(login_url="login"), name="dispatch")
class UserProfileView(View):
    template_name = "accounts/userprofile.html"

    def get(self, request):
        return render(request, self.template_name)


@method_decorator(login_required(login_url="login"), name="dispatch")
class LibrarianProfileView(View):
    template_name = "accounts/librarianprofile.html"

    def get(self, request):
        return render(request, self.template_name)


@method_decorator(login_required(login_url="login"), name="dispatch")
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
