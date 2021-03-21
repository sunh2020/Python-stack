from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # if request.method == "GET":
        return render(request, "index.html")
    # if request.method == "POST":
    #     print(request.POST['full_name'])
    #     print(request.POST['dojo_location'])
    #     print(request.POST['fav_lang'])
    #     return redirect("/login")

def create(request):
    dummy_info = {
        "context_name" : request.POST['full_name'],
        "context_location" : request.POST['dojo_location'],
        "context_language" : request.POST['fav_lang'],
        "context_option" : request.POST['option']
    }
    return render(request, "result.html", dummy_info)

def reset(request):
    request.session.clear()
    return redirect("/login")