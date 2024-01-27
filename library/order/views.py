from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Order
from .forms import OrderCreateForm


@method_decorator(login_required(login_url="login"), name="dispatch")
class AllOrdersView(View):
    template_path = "order/available_orders.html"

    def get(self, request):
        all_orders = Order.get_all_orders()
        context = {
            "all_orders": all_orders
        }
        return render(request, self.template_path, context)


class CreateOrderView(View):
    template_path = "order/order_creation_form.html"
    redirect_url = 'available_orders'
    order_creation_form = OrderCreateForm

    def get(self, request):
        order_creation_form = self.order_creation_form(initial={'user': request.user})
        context = {
            "order": order_creation_form
        }
        return render(request, self.template_path, context)

    def post(self, request):
        order_creation_form = self.order_creation_form(request.POST)
        if order_creation_form.is_valid():
            order_instance = order_creation_form.save(commit=False)
            order_instance.user = request.user
            order_instance.save()
            return redirect(self.redirect_url)

        context = {
            "order": order_creation_form
        }
        return render(request, self.template_path, context)
