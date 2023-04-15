from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    
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
    likes = models.ManyToManyField(User, related_name='book_likes', blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="Comments")
    name = models.CharField(max_length=75)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
