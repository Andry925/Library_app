from django.urls import path
from . import views

urlpatterns = [
    path("available_orders/", views.AllOrdersView.as_view(), name = "available_orders"),
]
