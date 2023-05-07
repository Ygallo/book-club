# Generated by Django 3.2.18 on 2023-05-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0010_alter_book_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookpoll',
            old_name='question',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='bookpoll',
            old_name='name',
            new_name='poll_title',
        ),
        migrations.RemoveField(
            model_name='bookpoll',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookpoll',
            name='description',
        ),
        migrations.AddField(
            model_name='bookpoll',
            name='books_selection',
            field=models.ManyToManyField(related_name='poll', to='bookclub.Book'),
        ),
    ]
