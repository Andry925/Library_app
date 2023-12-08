from django.shortcuts import redirect, render
from .forms import UserForm

# Create your views here.


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
            "user_form": user_form_with_data
        }
        return render(request, "accounts/register.html", context)
    user_form_with_data.save()
    return redirect("register")
