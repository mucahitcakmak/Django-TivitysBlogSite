from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(req):

    if req.method == "POST":
        username = req.POST.get("form3Example1cg", False)
        password = req.POST["form3Example4cg"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect("/")
        else:
            return redirect("login")
    else:
        return render(req, "user/loginPage.html")

def logout(req):
    if req.method == "POST":
        auth.logout(req)
    return redirect("/")

