from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Book, BookPoll, PollVote
from .forms import CommentForm, BookForm, PollForm
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

from django_currentuser.db.models import CurrentUserField
from django.urls import reverse_lazy

# Create your views here.


class Home(generic.TemplateView):
    """
    View to display the home page
    """
    template_name = "index.html"


class BookList(generic.ListView):
    """
    View to display recommended books
    """
    model = Book
    queryset = Book.objects.order_by('title')
    template_name = "books.html"
    paginate_by = 8


class BookDetail(View):
    """
    View to display books with full description, comments and likes.
    """
    def get(self, request, slug):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        comments = book.comments.filter(approved=True).order_by('created_on')
        liked = False
        if book.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "books_detail.html",
            {
                "book": book,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):
        queryset = Book.objects.all
        book = get_object_or_404(queryset, slug=slug)
        comments = book.comments.filter(approved=True).order_by(created_on)
        liked = False
        if book.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.name
            comment = comment_form.save(commit=False)
            comment.book = book
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "books_detail.html",
            {
                "book": books,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class MyBooks(generic.ListView):
    """
    View to display users' added books
    """

    model = Book
    queryset = Book.objects.order_by('title')
    template_name = "my_books.html"
    paginate_by = 8

    def get_queryset(self):
        return Book.objects.filter(created_by=self.request.user.id)    


class AddBook(generic.CreateView):
    """
    View to allow users once logged in to add a book
    """
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('my_books')
    
    def form_valid(self, form):
    # Save a new Listing object from the form's data.
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditBook(generic.UpdateView):
    """
    View that allows users to edit a book they had add to the club
    """
    model = Book
    form_class = BookForm
    template_name = 'edit_book.html'
    success_url = reverse_lazy('my_books')


class DeleteBook(generic.DeleteView):
    """
    View that allows users to delete a book they had add to the club
    """
    model = Book
    template_name = 'delete_book.html'
    success_message = "Book deleted successfully"
    success_url = reverse_lazy('my_books')


class BookPoll(generic.CreateView):
    """
    View to allow users create a book poll to choose what book
    to discuss
    """
    form_class = PollForm
    template_name = 'poll.html'


class PollVote(generic.CreateView):
    """
    View to allow users to vote on a book poll
    """
    model = PollVote
    template_name = 'poll.html'
    fields = '__all__'
    success_message = "Thank you for your vote!"
    success_url = reverse_lazy('books.html')

    def get(self, request):
        poll = Book.objects.all()

        return render(
            request,
            "poll.html",
            {
                "poll_title": poll_title,
                "books_selection": books_selection,
                "timestamp": timestamp,
            },
        )