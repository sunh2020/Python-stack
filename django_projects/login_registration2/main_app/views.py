from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    # 1. Validate user information
    # 2. User doesn't pass validation
    # 3. User doesn't pass validation
    errors = User.objects.user_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect("/")
    # 4. encrypt password    
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    print(hashed_pw)    
    new_user = User.objects.create(
        fname=request.POST['fname'],
        lname=request.POST['lname'],
        email=request.POST['email'],
        password=request.POST['password'],
        confirm_pw=request.POST['confirm_pw']
    )
    request.session['user_id'] = new_user.id
    return redirect("/success")

def success(request):
        context = {
            "user" : User.objects.get(id=request.session['user_id'])
        }
        return render(request, "success.html", context)

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.hashpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id']
            return redirect("/login")
        messages.error(request, "Invalid credentials")
        return redirect("/")
    messages.error(request, "Email doesn't exist, register an account")
    return redirect("/")    

def logout(request):
    return redirect("/")
    