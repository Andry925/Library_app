from django.urls import path
from . import views

urlpatterns = [
    path("available_orders/", views.AllOrdersView.as_view(), name = "available_orders"),
    path("create_order/", views.CreateOrderView.as_view(), name = "create_order")
]
