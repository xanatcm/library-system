from msilib.schema import ServiceInstall
from unicodedata import category
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from books.permissions import IsLibrarian
from .models import Author, Book, BookItem
from .serializers import AuthorSerializer, BookItemSerializer, BookSerializer, BookItemSerializerRetrieve
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarian]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'subject']


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [IsLibrarian]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BookItemSerializerRetrieve
        else:
            return BookItemSerializer

    @action(detail=False)
    def list_rent_books(self, request):
        books_items = BookItem.objects.filter(
            is_rent=True
        )
        serializer = BookItemSerializer(books_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["patch"], detail=True)
    def set_user_rent(self, request, pk):
        book_item = BookItem.objects.get(pk=pk)
        if book_item.reserve == None or book_item.reserve == User.objects.get(pk=request.data["rent"]):
            books_items = Book.objects.filter(
                bookitem__reserve_id=request.data["rent"]).count()
            if books_items >= 5:
                return Response({"message": "No puedes rentar mas de 5 libros"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(
                BookItem.objects.get(pk=pk),
                data=request.data, partial=True
            )
            if serializer.is_valid():

                self.perform_update(serializer)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.error, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Este libro está rentado por otro usuario"}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["patch"], detail=True)
    def set_user_reserve(self, request, pk):
        serializer = self.serializer_class(
            BookItem.objects.get(pk=pk),
            data=request.data, partial=True)
        if serializer.is_valid():

            self.perform_update(serializer)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarian]
