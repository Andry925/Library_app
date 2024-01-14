from django.shortcuts import render
from django.views import View
from .models import Order


class AllOrdersView(View):
    template_path = "order/available_orders.html"

    def get(self, request):
        all_orders = Order.get_all_orders()
        context = {
            "all_orders": all_orders
        }
        return render(request, self.template_path, context)
