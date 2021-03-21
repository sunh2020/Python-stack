from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")

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

# def dashboard(request):
#     c

# def displayShow(request, show_id):
#     context = {
#         "one_show" : Show.objects.get(show_id)
#     } 
#     return render(request, "show.html", context)




