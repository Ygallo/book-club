from .models import Comment, Book
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        description = SummernoteTextField()

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
        widgets = {
           'description': SummernoteWidget(),
         }
