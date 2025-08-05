from django.shortcuts import render

def ucak(request):
    return render(request, "uçuşlar/index.html")
