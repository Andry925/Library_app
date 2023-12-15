from django.urls import path 
from . import views

urlpatterns = [
    path("register/",views.RegistrationView.as_view(),name="register"),
    #path("login/",views.LoginView.as_view(), name ="login"),
    #path("logout/",views.logout_user,name="logout"),
    #path("librarian_profile/",views.redirect_librarian, name="librarian_profile"),
    #path("user_profile/", views.redirect_user, name = "user_profile")
    
]