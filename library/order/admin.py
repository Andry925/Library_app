from django.contrib import admin
from .models import Order


class TasksAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book")


admin.site.register(Order, TasksAdmin)
