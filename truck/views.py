from django.shortcuts import render
from django.http import HttpResponse
import datetime
from models import Trip


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
       road = Truck.objects.all().filter(trip_complete = False)
       context = {"road":road}


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
        #retun render()