from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def registration(request):
    user_form = UserForm()
    context = {
        "user_form":user_form
    }
    return render(request, "accounts/register.html",context)
