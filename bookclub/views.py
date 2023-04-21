from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book

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
    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        comments = book.comments.filter(approved=True).order_by(created_on)
        liked = False
        if post.likes.filter(id=self.user.id).exist():
            liked = True    
        
        return render(
            request,
            "book.detail.html",
            {
                "books": books,
                "comments": comments,
                "liked": liked
            }
        )

