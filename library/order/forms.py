from django import forms
from accounts.models import User
from book.models import Book
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
        days = cleaned_data.get('max_days_to_take_book')
        self.validate_book_amount(book_name=book, days=days)
        if Order.objects.filter(user=self.user, book=book).exists():
            raise forms.ValidationError("You can not book this book any more")

    def validate_book_amount(self, book_name, days):
        book = Book.objects.get(name=book_name)
        if book.count <= days:
            raise forms.ValidationError("We do not have such amount of books")
