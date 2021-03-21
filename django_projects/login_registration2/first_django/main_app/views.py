from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
def root(request): # set function name as root since it set on urls.py
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to later display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, num):
    return HttpResponse(f"placeholder to display blog number {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num} with a method named 'edit'")

def destroy(request, num):
    return redirect("/blogs")

# def hello(request):
#     # you're unauthorized to be here
#     return redirect("/error")

# def error(request):
#     return render(request, "error.html")