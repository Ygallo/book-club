from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books")

    LITERARY_FICTION = 'LF'
    MISTERY = 'MI'
    THRILLER = 'TR'
    HORROR = 'HR'
    HISTORICAL = 'HL'
    ROMANCE = 'RO'
    SCIENCE_FICTION = 'SF'
    FANTASY = 'FY'
    WOMENS_FICTION = 'WF'
    BLANK = 'BK'
    GENRE_CHOICES = [
        (LITERARY_FICTION, 'Literary_Fiction'),
        (MISTERY, 'Mistery'),
        (THRILLER, 'Thriller'),
        (HORROR, 'Horror'),
        (HISTORICAL, 'Historial'),
        (ROMANCE, 'Romance'),
        (SCIENCE_FICTION, 'Science_Fiction'),
        (FANTASY, 'Fantasy'),
        (WOMENS_FICTION, 'Womens_Fiction'),
        (BLANK, 'Blank')
    ]
    genre_choices = models.CharField(
        max_length=2,
        choices=GENRE_CHOICES,
        default=BLANK
        )
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='book_likes', blank=True)
    votes = models.ManyToManyField(User, related_name='votes', blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE,
            related_name="comments")
    name = models.CharField(max_length=75, default='Blank')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, default="empty")
    voter = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name="voter")

    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
