# Generated by Django 5.0 on 2023-12-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20, unique=True)),
                ('patronymic', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
