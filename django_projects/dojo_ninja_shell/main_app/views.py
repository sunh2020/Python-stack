from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        'main_app': Dojo.objects.all(),
        
    }
    return render(request, "index.html", context)

def add_dojo(request):
    new_dojo = Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )

    return redirect("/")

def add_ninja(request):
    # GET DO JO FROM DATABASE
    main_app = Dojo.objects.get(id = request.POST['dojo.id'])
    # CREATE A NEW NINJA
    new_ninja = Ninja.objects.create(
        first_Name = request.POST['first_name'],
        last_Name = request.POST['last_name'],
        dojo = request.POST['dojo'],
        creator = main_app
    )
    # print(new_ninja.id)
    return redirect("/") # redirect to URL

