from django import forms
from accounts.models import User
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["book", "max_days_to_take_book"]

    def __init__(self, *args, user=None, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].queryset = User.objects.filter(username=user)
