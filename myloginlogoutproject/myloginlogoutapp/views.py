from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    context = {
        "title": "User Management System",
        "welcome_message": "Welcome to the user management system.",
        "user_list": User.objects.all(),
        "user": request.user,
    }
    return render(request, "myloginlogoutapp/index.html", context)


@login_required()
def userdetail(request, username):
    # if request.user.is_anonymous:
    #     return HttpResponse("Error: Please login first!")
    #
    # user = authenticate(username=request.POST["username"], password=request.POST["password"])
    # if user:
    #     return redirect("/userdetail/" + username)
    # else:
    #     return HttpResponse("Error: Please login first!")

    context = {"user": User.objects.get_by_natural_key(username)}
    return render(request, "myloginlogoutapp/userdetail.html", context)


def signup(request):
    if request.method == "GET":
        return render(request, "myloginlogoutapp/signup.html")
    elif request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["user_password"]
        email = request.POST["user_email"]

        if username == "":
            return HttpResponse("Username is not specified.")
        if password == "":
            return HttpResponse("Password is not specified.")
        if email == "":
            return HttpResponse("Email is not specified.")

        # Add user in DB.
        User.objects.create_user(username=username, password=password, email=email)
        user = authenticate(username=username, password=password)
        if user:
            return redirect("index")
        else:
            return HttpResponse("Error: Unauthorized!")
    else:
        return HttpResponse("Method not supported.")


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
            #return redirect("/userdetail/" + username)
            return redirect("index")
        else:
            return HttpResponse("Error: Authentication failed!")


def signout(request):
    logout(request)
    return redirect("index")
