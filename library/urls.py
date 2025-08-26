from django.urls import path
from .views import create_book, create_author, get_book_by_id, get_author_by_id

urlpatterns = [
    path('createbook/', create_book, name='createbook'),
    path('createauthor/', create_author, name='createauthor'),
    path('getBookById/', get_book_by_id, name='getBookById'),
    path('getAuthorById/', get_author_by_id, name='getAuthorById')
]