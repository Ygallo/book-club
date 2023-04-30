from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BookForm(forms.MoldelForm):
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
            'created on',
        ]


class PollForm(forms.ModelForm):
    class Meta:
        model = BookPoll
        fields = [
            'name',
            'question',
            'book',
            'start_date',
            'end_date',
        ]