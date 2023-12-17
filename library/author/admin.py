from django.contrib import admin
from .models import Author


class TasksAdmin(admin.ModelAdmin):
    list_display = ("name","surname")


admin.site.register(Author, TasksAdmin)

