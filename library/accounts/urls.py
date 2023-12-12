from django.urls import path 
from . import views

urlpatterns = [
    path("register/",views.registration,name="register"),
    path("login/",views.login_user, name ="login"),
    path("userprofile/",views.dashboard, name="userprofile"),
    path("logout/",views.logout_user,name="logout")
]