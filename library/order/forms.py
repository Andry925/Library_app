from django import forms
from accounts.models import User
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["book", "max_days_to_take_book"]

    def __init__(self, *args, user=None, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.user = user
        if self.user:
            self.fields['user'].queryset = User.objects.filter(username=user)

    def clean(self):
        cleaned_data = super(OrderCreateForm, self).clean()
        book = cleaned_data.get('book')
        print(self.user)
        if Order.objects.filter(book=book).exists() and Order.objects.filter(user=self.user).exists():
            raise forms.ValidationError(
                "You can not book this book anymore"
            )
