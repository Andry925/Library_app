from django.urls import path 
from . import views

urlpatterns = [
    path("register/",views.RegistrationView.as_view(),name="register"),
    path("login/",views.LoginView.as_view(), name ="login"),
    path("user_profile/", views.UserProfileView.as_view(), name = "user_profile"),
    path("librarian_profile/",views.LibrarianProfileView.as_view(), name="librarian_profile"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    
   
    
]