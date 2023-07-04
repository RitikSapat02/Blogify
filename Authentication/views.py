from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_up(request):
    form = UserCreationForm()
    is_valid = False

    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            form.save()
            is_valid = True
    
    return render(request,'Authentication/sign_up.html',{
        'form':form,
        'is_valid':is_valid

    })
