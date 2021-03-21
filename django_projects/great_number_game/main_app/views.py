from django.shortcuts import render, redirect
import random
print(random.randint(1, 100))
# Create your views here.
def index(request):
    if "number" not in request.session:
        request.session["number"] = random.randint(1, 100)
    if "message" not in request.session:
        request.session["message"] = ""
    return render(request, "index.html")

def result(request):
    if int(request.POST["number"]) == request.session["number"]:
        request.session["message"] = "correct"
    if int(request.POST["number"]) < request.session["number"]:
        request.session["message"] = "low"
    if int(request.POST["number"]) > request.session["number"]:
        request.session["message"] = "high"
    return redirect("/")
 

def reset(request):
    request.session.clear()
    return redirect("/")
    
