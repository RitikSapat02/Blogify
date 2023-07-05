from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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


def sign_in(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    
    return render(request,'Authentication/login.html',context={
        'form':form,
    })


@login_required()
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))