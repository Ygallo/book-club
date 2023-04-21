from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('books/', views.BookList.as_view(), name='books'),
    path('books_detail/', views.BookDetail.as_view(), name='books_details')
]
