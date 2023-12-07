from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Mete:
        model = User
        fields = ["email","first_name","last_name","username","role","password"]