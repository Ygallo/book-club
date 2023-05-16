from .models import Comment, Book
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 10})

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
