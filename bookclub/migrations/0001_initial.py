# Generated by Django 3.2.18 on 2023-04-15 18:51

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('author', models.CharField(max_length=250)),
                ('genre_choices', models.CharField(choices=[('LF', 'Literary_Fiction'), ('MI', 'Mistery'), ('TR', 'Thriller'), ('HR', 'Horror'), ('HL', 'Historial'), ('RO', 'Romance'), ('SF', 'Science_Fiction'), ('FY', 'Fantasy'), ('WF', 'Womens_Fiction'), ('BK', 'Blank')], default='BK', max_length=2)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('description', models.TextField()),
                ('likes', models.ManyToManyField(blank=True, related_name='book_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='bookclub.book')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
