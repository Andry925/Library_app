from django.urls import path
from . import views

urlpatterns = [
    path("authors/",views.index,name="all_authors"),
]