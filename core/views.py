from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from books.models import Book
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from books.serializers import BookSerializer

from core.permissions import IsOwner
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]

    @action(detail=True)
    def my_rents(self, request, pk):
        books = Book.objects.filter(
            bookitem__rent=pk
        )
        serializer = BookSerializer(books, many=True)
        try:
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_200_OK)

    @action(detail=True)
    def my_reservations(self, request, pk):
        books = Book.objects.filter(
            bookitem__reserve=pk
        )
        serializer = BookSerializer(books, many=True)
        try:
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_200_OK)
