from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .form import RegistrationForm


# Create your views here.

def signup(request):
    if request == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render('next')
    else:
        return render(request, 'login.html', )
    
