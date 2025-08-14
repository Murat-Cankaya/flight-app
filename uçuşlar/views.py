from django.shortcuts import render

def ucak(request):
    return render(request, "uçuşlar/index.html")
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Flight

@login_required
def main_page(request):
    flights = Flight.objects.order_by("sch_dep_dt", "sch_dep_tm")
    
    return render(request, "account/main_page.html", {"flights": flights})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight
from .forms import FlightForm

@login_required
def flight_create(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:main_page")
    else:
        form = FlightForm()
    return render(request, "uçuşlar/flight_form.html", {"form": form, "title": "Add Flight"})

@login_required
def flight_update(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect("account:main_page")
    else:
        form = FlightForm(instance=flight)
    return render(request, "uçuşlar/flight_form.html", {"form": form, "title": f"Edit Flight {flight.flt_no}"})

@login_required
def flight_delete(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == "POST":
        flight.delete()
        return redirect("account:main_page")
    return render(request, "uçuşlar/flight_confirm_delete.html", {"flight": flight})
