"""
TODO: file description

2023-05-19 - Nathaniel mason : add create_user view

"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import JEANZUserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "users/index.html")

def create_user(request):
    if request.method != 'POST':
        form = JEANZUserCreationForm()
    else:
        form = JEANZUserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account Created Successfully!")
            form.save(True) # commit defined as True, so will immediately store in the DB
            return redirect('users:index')
        else:
            print(form.errors)
            messages.error(request, "User information not valid")
            return redirect('users:create_user')

    context = {'userform': form}

    return render(request, 'users/create_user.html', context)
