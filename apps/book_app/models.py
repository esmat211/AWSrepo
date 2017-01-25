from __future__ import unicode_literals

from django.db import models

class BookManager(models.Manager):
    def add_book(self, postData):
        print postData
        # validations
        author = Author.objects.get(id=postData['author_id'])
        book = self.create(title = postData['title'], author = author)
        print book
    def validate_book(self, postData):

        pass

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, related_name= 'books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    objects = BookManager()
