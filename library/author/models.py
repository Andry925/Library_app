from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, unique=True)
    patronymic = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname}"

    @staticmethod
    def get_author_by_id(pk):
        try:
            return Author.objects.get(pk=pk)

        except Author.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(pk):
        try:
            author = Author.objects.get(pk=pk)
            author.delete()
            return True
        except Author.DoesNotExist:
            return False

    @staticmethod
    def is_valid_length(value, max_length):
        return value and len(value) <= max_length

    @staticmethod
    def create_author(name, surname, patronymic):
        if Author.is_valid_length(name,20) and Author.is_valid_length(surname,20):
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author

    def update_author(self, name=None, surname=None, patronymic=None):
        if Author.is_valid_length(name, 20):
            self.name = name

        if Author.is_valid_length(surname, 20):
            self.surname = surname

        self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all_authors():
        return Author.objects.all()
