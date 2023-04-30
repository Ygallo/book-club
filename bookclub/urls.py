from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<slug:slug>/', views.BookDetail.as_view(),
         name='books_detail'),
    path('addbook/', views.AddBook.as_view(), name='add_book')
]
