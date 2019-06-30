from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Trip


def index(request):
    return HttpResponse("Welcome to Transport Management")


def dashboard(request):
    road = None
    if request.method == "POST":
        start_date = request.POST.get("startdate")
        end_date = request.POST.get("enddate")
        truck = request.POST.get("truck")
        if start_date and end_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__gte = start_date, trip_start_date__lte = end_date, truck = truck)
                context = {"road":road}
                return render(request, "detail.html", context)
            else:
                road = Trip.objects.all().filter(trip_start_date__gte = start_date, trip_start_date__lte = end_date)
                context = {"road":road}
                return render(request, "dashboard.html", context)
        if start_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__gte = start_date, truck = truck)
            else:
                road = Trip.objects.all().filter(trip_start_date__gte = start_date)
            context = {"road":road}
            return render(request, "dashboard.html", context)

        if end_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__lte = end_date, truck = truck)
            else:
                road = Trip.objects.all().filter(trip_start_date__lte = end_date)
            context = {"road":road}
            return render(request, "dashboard.html", context)

        if truck:
            road = Trip.objects.all().filter(truck = truck)
            context = {"road":road}
            return render(request,"dashboard.html",context)
            

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
        comment = request.POST.get("comment")
        expense = request.POST.get("expense")
        if expense:
            expense = float(expense)
        else:
            expense = 0.0
        weight = float(weight)
        cost = float(cost)
        total_cost = weight*cost

        #save the data
        t = Trip(truck=truck, trip_start_date=trip_start_date, trip_start_time=trip_start_time, source=source, destination=destination, driver=driver, item=item, consignee=consignee, weight=weight, cost_per_ton=cost, total_cost=total_cost, comment=comment, expense=expense)
        t.save()

        return HttpResponseRedirect('')

    else:
        return render(request,"new.html")

def update_trip(request):
    if request.method == "POST":
        truck = request.POST.get("truck")
        print(truck)
        expense = request.POST.get("expense")
        comment = request.POST.get("comment")
        trip_end_date = request.POST.get("trip_end_date")
        trip_end_time = request.POST.get("trip_end_time")
        if expense:
            t = Trip.objects.filter(truck=truck, trip_complete=False)
            print(t)
            exp = t[0].expense+float(expense)
            comm = t[0].comment+'\n'+comment
            Trip.objects.filter(truck=truck, trip_complete=False).update(expense=exp, comment=comm)
        if trip_end_date and trip_end_time:
            Trip.objects.filter(truck=truck, trip_complete=False).update(trip_end_date=trip_end_date, trip_end_time=trip_end_time, trip_complete = True)
        return HttpResponseRedirect('')
    else:
        return render(request,"update.html")