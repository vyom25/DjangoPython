from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import BookSerializer, AuthorSerializer
from .models import Book, Author
# Create your views here.


@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)

    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)

    if author_serializer.is_valid():
        author_serializer.save()
        return Response(author_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_book_by_id(request):
    id = request.GET.get('id')
    print(id)
    book = Book.objects.get(pk=id)

    serializer = BookSerializer(book)

    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_author_by_id(request):
    id = request.GET.get('id')
    print(id)
    book = Author.objects.get(pk=id)

    serializer = AuthorSerializer(book)

    return Response(serializer.data, status=status.HTTP_200_OK)



