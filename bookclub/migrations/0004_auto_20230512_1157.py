# Generated by Django 3.2.18 on 2023-05-12 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookclub', '0003_auto_20230512_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='voter',
        ),
        migrations.AddField(
            model_name='choice',
            name='voter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='voter', to=settings.AUTH_USER_MODEL),
        ),
    ]
