# Generated by Django 3.2.18 on 2023-04-16 12:04

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0003_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
    ]
