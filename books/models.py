from platform import release
import uuid
from django.db import models
from libraries.models import Rack
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=250)
    desciption = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.id}| {self.name}"


class Book(models.Model):

    isbn = models.CharField(max_length=11, unique=True)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.title} | {self.author.name}"


class BookItem(models.Model):

    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)
    reserve = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, related_name="reserve", blank=True)
    is_reserve = models.BooleanField(default=False)
    rent = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, related_name="rent", blank=True)
    is_rent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} | {self.book.title}"
