from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=20)
    author_surname = models.CharField(max_length=20, unique=True)
    patronymic = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return f"{self.author_name} {self.author_surname}"
