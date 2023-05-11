from .models import Comment, Book
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'slug',
            'author',
            'genre_choices',
            'image',
            'description',
            'image',
        ]


# class PollForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = [
#             'poll_title',
#             #'notes',
#             #'books_selection',
#             'start_date',
#             'end_date',
#         ]