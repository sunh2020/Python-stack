from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def index(request):
    context = {
        'main_app': Users.objects.all() # 'main_app' is key, which can be any name, however got to match with html function name
    }
    return render(request, "index.html", context)

def add_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    age = request.POST['age']
    Users.objects.create(
        first_name = first_name, 
        last_name = last_name,
        email = email, 
        age = age)
    return redirect("/")