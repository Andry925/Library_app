from datetime import timedelta
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import User
from book.models import Book


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user")
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="book")
    borrowed_at = models.DateTimeField(auto_now_add=True)
    max_days_to_take_book = models.IntegerField(
        default=0, validators=[
            MinValueValidator(0), MaxValueValidator(30)])
    expired_at = models.DateTimeField(default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.expired_at:
            self.expired_at = self.calculate_expired_date()
        super().save(*args, **kwargs)

    def calculate_expired_date(self):
        expire_date = self.borrowed_at + \
            timedelta(days=self.max_days_to_take_book)
        return expire_date
