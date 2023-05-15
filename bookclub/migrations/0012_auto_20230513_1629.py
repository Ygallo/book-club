# Generated by Django 3.2.18 on 2023-05-13 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0011_monthlybook'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOfTheMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_book', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='bookclub.book')),
            ],
        ),
        migrations.DeleteModel(
            name='MonthlyBook',
        ),
    ]