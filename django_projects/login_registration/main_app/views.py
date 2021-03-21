from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    User.objects.user_validator(request.POST)
    context = {
        'main_app' : User.objects.all()
    }
    return render(request, "index.html", context)

def process_user(request):
    # 1. Validate user information
    errs = User.objects.user_validator(request.POST)
    if len(errs) > 0: # same as if errs: - when this is empty, it means valid and pass
        for msg in errs.values():
            messages.error(request, msg)
        return redirect("/")
    # User passes validation        
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    print(hashed_pw)    
    new_user = User.obejcts.create(
        fname=request.POST['fname'],
        lname=request.POST['lname'],
        fav_color=request.POST['fav_color'],
        email=request.POST['email'],
    )
  
    # Store new user's ID in session
    request.session['user_id'] = new_user.id
    # Redirect you to dashboard
    return redirect("/")
    def dashboard(request):
         