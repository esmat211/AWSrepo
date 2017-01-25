from django.shortcuts import render, redirect
from .models import Author, Book
from ..publisher.models import Publisher

# Create your views here.
def index(request):
    print Author.objects.all()
    context = {
    'all_authors': Author.objects.all(),
    'all_books': Book.objects.all(),
    'all_publishers': Publisher.objects.all(),
    }
    return render(request, 'book_app/index.html', context)

def create_author(request):
    Author.objects.create(name = request.POST['name'])
    print request.POST['name']
    return redirect('/')

    #add author with book
def create_book(request):
    author = Author.objects.get(id = request.POST['author'])
    Book.objects.create(title = request.POST['title'], author = author)
    return redirect('/')

def add_book(redirect):
    if request.method == 'POST':
        # print request.POST
        Book.objects.add_book(request.POST)

    return redirect('books:index')
