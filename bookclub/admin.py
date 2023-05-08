from django.contrib import admin
from .models import Book, Comment, Question, Choice
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    propopulated_fields = {'slug': ('title',)}
    list_filter = ('genre_choices', 'author', 'created_on')
    search_fields = ('title', 'genre')
    list_display = ('title', 'genre_choices', 'author')
    summernote_fields = ('description', 'excerpt')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approved_comment']

    def approved_comment(self, request, queryset):
        queryset.update(approve=True)


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class PollAdmin(SummernoteModelAdmin):

    # list_display = ('poll_title', 'start_date', 'end_date')
    # list_filter = ('poll_title', )
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


