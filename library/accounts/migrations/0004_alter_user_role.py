# Generated by Django 5.0 on 2023-12-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('User', 'User'), ('Librarian', 'Librarian')]),
        ),
    ]
