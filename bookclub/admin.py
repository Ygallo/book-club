from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    # propopulated_fields = {'slug': ('title',)}
    list_filter = ('genre_choices', 'author')
    search_fields = ('title', 'genre')
    list_display = ('title', 'genre_choices', 'author')
    summernote_fields = ('description')


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):

#     list_display = ('name', 'body', 'created_on', 'approved')
#     list_filter = ('approved', 'created_on')
#     search_fields = ('name', 'email', 'body')

# @admin.register(BookPoll)
# class PollAdmin(admin.ModelAdmin):

#     list_display = ('question', 'start_date', 'end_date')
#     list_filter = ('book')
#     search_fields = ('book', 'question')