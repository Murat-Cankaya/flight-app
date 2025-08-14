from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from uçuşlar.models import Flight


@login_required
def main_page(request):
     flights = Flight.objects.all().order_by("sch_dep_dt", "sch_dep_tm")
     return render(request, "account/main_page.html", {"flights": flights})
    

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account:main_page") 
        else:
            return render(request, "account/login.html", {"error": "Invalid username or password"})
    return render(request, "account/login.html")

def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html", {"error": "username is already used."})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html", {"error": "email is already used."})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return redirect("account:main_page")
        else:
            return render(request, "account/register.html", {"error": "Passwords do not match"})
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("account:login")




