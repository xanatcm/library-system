from rest_framework import serializers

from core.serializers import UserSerializer
from .models import Author, Book, BookItem


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"
        depth = 1


class BookItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    rent = UserSerializer()

    class Meta:
        model = BookItem
        fields = "__all__"
        depth = 1


class BookItemSerializerRetrieve(serializers.ModelSerializer):
    book = BookSerializer()
    rent = UserSerializer()

    class Meta:
        model = BookItem
        fields = "__all__"
