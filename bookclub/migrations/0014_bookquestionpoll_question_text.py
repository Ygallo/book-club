# Generated by Django 3.2.18 on 2023-05-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0013_auto_20230507_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookquestionpoll',
            name='question_text',
            field=models.CharField(default='Blank', max_length=200),
        ),
    ]