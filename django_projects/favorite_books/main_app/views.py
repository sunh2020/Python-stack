from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.user_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect("/")
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    print(hashed_pw)    
    new_user = User.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        password=hashed_pw,
        confirm_pw=hashed_pw
    )
    request.session['user_id'] = new_user.id
    return redirect("/books") 

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/books")
        messages.error(request, "Invalid credentials")
        return redirect("/")
    messages.error(request, "Email doesn't exist, register an account")
    return redirect("/")

def books(request):
    context = {
       "books" : Book.objects.all()
       }
    return render(request, "books.html", context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    print(errors)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect("/books")
        
    new_book = Book.objects.create(    
        title = request.POST['title'],
        desc = request.POST['description'],
        uploaded_by = User.objects.get(id=request.session['user_id'])
    )
    return redirect(F"/books/{new_book.id}")  

def created(request, id):
    return redirect("/books")      
   
def book_details(request, id):
    context = {
        'this_book' : Book.objects.get(id=id)
    
    }
    return render(request, "details.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")    

  

