from django.shortcuts import render, redirect
from django.views import View
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
            return redirect("register")
        context = {"registration_form": registration_form}
        return render(request, self.template_name, context)

    def hash_password(self, valid_user_form):
        password = valid_user_form.cleaned_data.get("password")
        user = valid_user_form.save(commit=False)
        user.set_password(password)
        return user
