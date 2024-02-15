from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from book.models import Book
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
        order_creation_form = self.order_creation_form()
        context = {
            "order": order_creation_form
        }
        return render(request, self.template_path, context)

    def post(self, request):
        order_creation_form = self.order_creation_form(request.POST)
        order_creation_form.user = request.user
        if order_creation_form.is_valid():
            order_instance = order_creation_form.save(commit=False)
            self.minus_book(order_create_form=order_creation_form)
            order_instance.user = request.user
            order_instance.save()
            return redirect(self.redirect_url)
        context = {
            "order": order_creation_form
        }
        return render(request, self.template_path, context)

    def minus_book(self, order_create_form):
        book_name = order_create_form.cleaned_data.get('book')
        amount_book = order_create_form.cleaned_data.get('max_days_to_take_book')
        book_instance = Book.objects.get(name=book_name)
        book_instance.count -= amount_book
        book_instance.save()
