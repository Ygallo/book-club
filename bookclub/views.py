from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Book, Question, Choice, Vote, BookOfTheMonth
from .forms import CommentForm, BookForm
from django.template import loader
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib import messages

# Create your views here


class Home(generic.TemplateView):
    """
    View to display the home page
    """
    template_name = "index.html"


class BookList(generic.ListView):
    """
    View to display recommended books
    """
    chosen = BookOfTheMonth.objects.all()
    model = Book
    queryset = Book.objects.order_by('title')
    template_name = "books.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context.update({'chosen_book': self.chosen})
        return context


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


class MyBooks(LoginRequiredMixin, generic.ListView):
    """
    View to display users' added books
    """

    model = Book
    queryset = Book.objects.order_by('title')
    template_name = "my_books.html"
    paginate_by = 8

    def get_queryset(self):
        return Book.objects.filter(created_by=self.request.user.id)


class AddBook(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    View to allow users once logged in to add a book
    """
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('my_books')
    success_message = "The book was added successfully"

    def form_valid(self, form):
        # Save a new Listing object from the form's data.
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditBook(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """
    View that allows users to edit a book they had add to the club
    """
    model = Book
    form_class = BookForm
    template_name = 'edit_book.html'
    success_url = reverse_lazy('my_books')
    success_message = "Your book was edited!"


class DeleteBook(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    """
    View that allows users to delete a book they had add to the club
    """
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('my_books')
    success_message = "The book deleted successfully"

    def delete(self, request, *args, **kwargs):
        """
        Code for success message take from python tutorial and stackoverflow
        """
        messages.success(self.request, self.success_message)
        return super(DeleteBook, self).delete(request, *args, **kwargs)


class BookLike(View):
    """
    View that allows users to like a book in the club
    """

    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        if book.likes.filter(id=request.user.id).exists():
            book.likes.remove(request.user)
        else:
            book.likes.add(request.user)

        return HttpResponseRedirect(reverse('books_detail', args=[slug]))


class BookVote(View):
    """
    View that allows users to vote on a book
    """

    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        if book.vote.filter(id=request.user.id).exists():
            book.vote.remove(request.user)
        else:
            book.vote.add(request.user)

        return HttpResponseRedirect(reverse('books_detail', args=[slug]))


# Get lastest question and display it

def poll(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# Show specific question and choices
@login_required(redirect_field_name="account_login")
def detail(request, question_id):

    try:
        question = get_object_or_404(Question, pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


# Get question and display results
def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# Vote for a question choice
@login_required(redirect_field_name="account_login")
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Check if the user has already voted for this question
    for choice in question.choice_set.all():

        if choice.vote_set.filter(user=request.user).exists():

            # If the user has already voted, display an error message
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You have already voted on this question.",
            })

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # Create a new Vote object to associate with the user and the question
        vote = Vote(user=request.user, choice=selected_choice)
        vote.save()

        return HttpResponseRedirect(reverse('results', args=(question.id, )))

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
