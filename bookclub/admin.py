from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
