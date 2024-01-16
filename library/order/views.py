from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Order


@method_decorator(login_required(login_url="login"), name="dispatch")
class AllOrdersView(View):
    template_path = "order/available_orders.html"

    def get(self, request):
        all_orders = Order.get_all_orders()
        context = {
            "all_orders": all_orders
        }
        return render(request, self.template_path, context)
