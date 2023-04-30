from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Book
from .forms import CommentForm, 

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
        #if book.likes.filter(id=self.user.id).exist():
           # liked = True    

        return render(
            request,
            "books_detail.html",
            {
                "book": book,
                "comments": comments,
                "commented": False,
                "liked": liked,
                # "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):
        queryset = Book.objects.all
        book = get_object_or_404(queryset, slug=slug)
        comments = book.comments.filter(approved=True).order_by(created_on)
        liked = False
        if post.likes.filter(id=self.user.id).exist():
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


class AddBook(generic.CreateView):
    """
    View to allow users once logged in to add a book
    """
    form_class = BookForm
    template_name = 'add_book.html'

