from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")

def addShow(request):
    return redirect("/")

def create(request):
    # 1. Validate your post information
    errors = Show.objects.validate_show(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    # 2. If validation pass, create show     
    new_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect(f"/shows/{new_show.id}")

def dashboard(request):
    # reading information
    context ={
        "main_app" : Show.objects.all()
    }
    return render(request, "dashboard.html", context)

def displayShow(request, show_id):
    # Reading, retreving information
    context ={
        "one_show" : Show.objects.get(id = show_id)
    }
    return render(request, "show.html", context)

def editShow(request, show_id):
    context ={
        "one_show" : Show.objects.get(id = show_id)
    }
    return render(request, "edit.html", context)

def updateShow(request, show_id):
    # 1. Validate your post information
    errors = Show.objects.validate_show(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit")
    # If validations pass update the show
    # Step 1. Grab show from DB  
    update_show = Show.objects.get(id = show_id)
    # Step 2. Change the information
    update_show.title=request.POST['title']
    update_show.network=request.POST['network'] 
    update_show.release_date=request.POST['release_date'] 
    update_show.description=request.POST['description'] 
    # Step 3. Save the updated show
    update_show.save()
    return redirect(f"/shows/{show_id}")        

def deleteShow(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect("/shows")

