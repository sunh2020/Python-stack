from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        'main_app': Book.objects.all(),
        
    }
    return render(request, "index.html", context)

def author2(request):
    context = {
       
        'main_app': Author.objects.all(),
    }
    return render(request, "author2.html", context)

def add_book(request):
    new_book = Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
    )
    return redirect("/")

def add_author(request):
    new_author = Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
    )
    return redirect("/")
    
def result_book(request, id):
    context = {
        'this_book': Book.objects.get(id=id),
        'all_authors' : Author.objects.all()
      
    }
    return render(request, "result.html", context)
    
def result_author(request, id):
    context = {
        'this_author': Author.objects.get(id=id),
        'all_books' : Book.objects.all()
      
    }
    return render(request, "result2.html", context)

def addBook(request):
    author = Author.objects.get(id=request.POST['author_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    book.authors.add(author)
    book.save()
    return redirect("/")

def addAuthor(request):
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST['author_id'])
    author.books.add(book)
    author.save()
    return redirect("/")

