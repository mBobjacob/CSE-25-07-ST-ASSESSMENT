from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserAuthenticationForm, UserForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render (request, 'registration.html', context)

def login_user(request):
    if request.method == "POST":
        form = UserAuthenticationForm(request,data=request.Post)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('')
    else:
        form = UserAuthenticationForm()
    context = {
        'form': form
    }
    return render (request, 'login.html', context)

