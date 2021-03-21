from django.shortcuts import render, redirect
import random
print(random.randint(0, 50))

# Create your views here.
def index(request):
    if "golds" not in request.session:
        request.session['golds'] = 0
    if "activities" not in request.session:
        request.session['activities'] = ""
    return render(request, "index.html")

def gold(request):
    prop = request.POST['which_form']
    if prop == 'farm':
       gold_earned = random.randint(10, 21) 
       request.session['golds'] += gold_earned
       request.session['activities'] += f"Earned {gold_earned} at the farm! \n"
    if prop == 'cave':
       gold_earned = random.randint(5, 11)
       request.session['golds'] += gold_earned 
       request.session['activities'] += f"Earned {gold_earned} at the farm! \n"

    if prop == 'house':
       gold_earned = random.randint(2, 6)
       request.session['golds'] += gold_earned 
       request.session['activities'] += f"Earned {gold_earned} at the farm! \n"

    if prop == 'casnio':
       gold_earned = random.randint(0, 50)
       request.session['golds'] += gold_earned  
       request.session['activities'] += f"Earned {gold_earned} at the farm! \n"
    return redirect("/")

    