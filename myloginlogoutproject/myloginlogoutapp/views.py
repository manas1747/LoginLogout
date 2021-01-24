from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .decorators import unauthenticated_user, allowed_roles
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    context = {
        "title": "User Management System",
        "welcome_message": "Welcome to the user management system.",
        "user_list": User.objects.all(),
        "user": request.user,
    }
    return render(request, "myloginlogoutapp/index.html", context)


@login_required
@allowed_roles(["manas_customer", "manas_admin"])
def userdetail(request, username):
    # if request.user.is_anonymous:
    #     return HttpResponse("Error: Please login first!")
    #
    # user = authenticate(username=request.POST["username"], password=request.POST["password"])
    # if user:
    #     return redirect("/userdetail/" + username)
    # else:
    #     return HttpResponse("Error: Please login first!")

    if request.method == "GET":
        context = {"user": User.objects.get_by_natural_key(username)}
        return render(request, "myloginlogoutapp/userdetail.html", context)


@unauthenticated_user
def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "myloginlogoutapp/signup.html", {"form": form})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Associate user to manas_customer group
            group = Group.objects.get(name="manas_customer")
            user.groups.add(group)
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid input.")


@unauthenticated_user  # implemented by manas in decorators.py
def signin(request):
    if request.method == "GET":
        return render(request, "myloginlogoutapp/signin.html")
    elif request.method == "POST":
        username = request.POST["user_name"]
        if username == "":
            return HttpResponse("Error: Username can not be empty!")

        password = request.POST["user_password"]
        if password == "":
            return HttpResponse("Error: Password can not be empty!")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            return HttpResponse("Error: Authentication failed!")


def signout(request):
    logout(request)
    return redirect("index")
