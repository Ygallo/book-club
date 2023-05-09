from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Book, Question, Choice
from .forms import CommentForm, BookForm
from django.template import loader
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

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
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        comments = book.comments.filter(approved=True).order_by('created_on')
        liked = False
        if book.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.book = book
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "books_detail.html",
            {
                "book": book,
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


class BookLike(View):
    
    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        if book.likes.filter(id=request.user.id).exists():
            book.likes.remove(request.user)
        else:
            book.likes.add(request.user)

        return HttpResponseRedirect(reverse('books_detail', args=[slug]))
    

class BookVote(View):
    
    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        if book.vote.filter(id=request.user.id).exists():
            book.vote.remove(request.user)
        else:
            book.vote.add(request.user)

        return HttpResponseRedirect(reverse('books_detail', args=[slug]))

# class PollVote(generic.ListView):
#     """
#     View to allow users to vote on a book poll
#     """
#     model = PollChoice
#     template_name = 'poll.html'
#     queryset = Book.objects.order_by('title')
#     fields = '__all__'
#     success_message = "Thank you for your vote!"
#     success_url = reverse_lazy('books.html')


# Get questions and display them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and choices


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=Question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Get question and display results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id, )))
