from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Trip, Truck


def index(request):
    return HttpResponse("Welcome to Transport Management")


def dashboard(request):
    if request.method == "POST":
        date = request.POST.get("date")
        truck = request.POST.get("truck")
        if date:
            if truck:
                road = Trip.objects.all().filter(start_date = date, truck = truck)
                context = {"road":road}
            else:
                road = Trip.objects.all().filter(start_date = date)
                context = {"road":road}
            #return render()
        if truck:
            road = Trip.objects.all().filter(truck = truck)

    else:
       road = Trip.objects.all().filter(trip_complete = False)
       context = {"road":road}
    return render(request, "dashboard.html", context)


def new_trip(request):
    if request.method == "POST":
        truck = request.POST.get("truck")
        trip_start_date = request.POST.get("trip_start_date")
        trip_start_time = request.POST.get("trip_start_time")
        source = request.POST.get("source")
        destination = request.POST.get("destination")
        driver = request.POST.get("driver")
        item = request.POST.get("item")
        consignee = request.POST.get("consignee")
        weight = request.POST.get("weight")
        cost = request.POST.get("cost")
        total_cost = float(weight)*float(cost)
        #save the data
        t = Trip(truck=truck, trip_start_date=trip_start_date, trip_start_time= trip_start_time, source=source, destination=destination, driver=driver, item=item, consignee=consignee, weight=weight, cost_per_ton = cost, total_cost=total_cost)
        t.save()
        #return render()

    else:
        return HttpRespnse("You are at New Trip Page")

def update_trip(request):
    if request.method == "POST":
        truck = request.POST.get("truck")
        expense = request.POST.get("expense")
        comment = request.POST.get("comment")
        trip_end_date = request.POST.get("trip_end_date")
        trip_end_time = request.POST.get("trip_end_time")
        if expense:
            t = Trip.objects.filter(truck=truck, trip_complete=False)
            exp = t.expense+expense
            comm = t.comment+'\n'+comment
            Trip.objects.filter(truck=truck, trip_complete=False).update(expense=exp, comment=comm)
        if trip_end_date and trip_end_time:
            Trip.objects.filter(truck=truck, trip_complete=False).update(trip_end_date=trip_end_date, trip_end_time=trip_end_time, trip_complete = True)

    else:
        return HttpResponse("You are at Update Trip page")


def show_trucks(request):
    trucks = Truck. objects.all()
    return render(request, "trucks.html", {"trucks":trucks})