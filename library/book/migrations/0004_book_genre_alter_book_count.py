# Generated by Django 5.0 on 2023-12-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
