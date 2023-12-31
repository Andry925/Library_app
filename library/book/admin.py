from django.contrib import admin
from .models import Book

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ("id","name","author")

admin.site.register(Book,TasksAdmin)

