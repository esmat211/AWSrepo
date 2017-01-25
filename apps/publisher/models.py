from __future__ import unicode_literals
from ..book_app.models import Book

from django.db import models
#Create your models here.
class PublisherManager(models.Manager):
    def add_publisher(self, postData):
        self.create(name = postData['name']),

    def add_book_to_publisher(self, postData):
        book = Book.objects.get(id = postData['book'])
        publisher = self.get(id = postData['publisher'])
        publisher.books.add(book)
        publisher.save()

class Publisher(models.Model):
    name = models.CharField(max_length = 45)
    books = models.ManyToManyField(Book, related_name = 'publisher')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = PublisherManager()
