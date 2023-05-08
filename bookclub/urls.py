from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<slug:slug>/', views.BookDetail.as_view(),
         name='books_detail'),
    path('addbook/', views.AddBook.as_view(), name='add_book'),
    path('mybooks/', views.MyBooks.as_view(), name='my_books'),
    path('test/', views.Test, name='test'),
    path('books/<slug:slug>/edit', views.EditBook.as_view(), name='edit_book'),
    path('books/<slug:slug>/delete', views.DeleteBook.as_view(), name='delete_book'),
    path('polls/', views.index, name='polls'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

