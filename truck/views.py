from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from .models import Trip, Expenses


def index(request):
    return HttpResponse("Welcome to Transport Management")

@login_required
def dashboard(request):
    road = None
    total_sale = 0.0
    total_expense = 0.0
    if request.method == "POST":
        start_date = request.POST.get("startdate")
        end_date = request.POST.get("enddate")
        truck = request.POST.get("truck").upper()
        if start_date and end_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__gte = start_date, trip_start_date__lte = end_date, truck = truck)
                expenses = Expenses.objects.all().filter(expense_date__gte = start_date, expense_date__lte = end_date, truck = truck)
                for r in road:
                    total_sale = total_sale+r.total_cost
                for e in expenses:
                    total_expense = total_expense+e.expenses
                
                context = {"road":road, "total_sale":total_sale, "expenses":expenses, "total_expense":total_expense}
                return render(request, "detail.html", context)
            else:
                road = Trip.objects.all().filter(trip_start_date__gte = start_date, trip_start_date__lte = end_date)
                expenses = Expenses.objects.all().filter(expense_date__gte = start_date, expense_date__lte = end_date)
        
        if start_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__gte=start_date, truck=truck)
                expenses = Expenses.objects.all().filter(expense_date__gte = start_date, truck = truck)
            else:
                road = Trip.objects.all().filter(trip_start_date__gte=start_date)
                expenses = Expenses.objects.all().filter(expense_date__gte = start_date)

        if end_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__lte = end_date, truck = truck)
                expenses = Expenses.objects.all().filter(expense_date__lte = end_date, truck = truck)
            else:
                road = Trip.objects.all().filter(trip_start_date__lte = end_date)
                expenses = Expenses.objects.all().filter(expense_date__lte = end_date)
    
        if truck:
            road = Trip.objects.all().filter(truck=truck)
            expenses = Expenses.objects.all().filter(truck = truck)
        
        for r in road:
            total_sale = total_sale+r.total_cost
        for e in expenses:
            total_expense = total_expense+e.expense
        context = {"road":road, "expenses":expenses ,"truck":truck, "start_date":start_date, "end_date":end_date, "total_sale":total_sale, "total_expense":total_expense}
        return render(request,"dashboard.html",context)

    else:
        road = Trip.objects.all().filter(trip_start_date = datetime.datetime.now().strftime('%Y-%m-%d') )
        expenses = Expenses.objects.all().filter(expense_date = datetime.datetime.now().strftime('%Y-%m-%d'))
        for r in road:
            total_sale = total_sale+r.total_cost
        for e in expenses:
            total_expense = total_expense+e.expense
        context = {"road":road, "expenses":expenses, "total_sale":total_sale, "total_expense": total_expense}
        return render(request, "dashboard.html", context)

@login_required
def new_trip(request):
    if request.method == "POST":
        truck = request.POST.get("truck").upper()
        trip_start_date = request.POST.get("trip_start_date")
        trip_start_time = request.POST.get("trip_start_time")
        source = request.POST.get("source")
        destination = request.POST.get("destination")
        driver = request.POST.get("driver")
        item = request.POST.get("item")
        consignee = request.POST.get("consignee")
        weight = request.POST.get("weight")
        cost = request.POST.get("cost")
        #comment = request.POST.get("comment")
        #expense = request.POST.get("expense")
<<<<<<< HEAD
    
=======
>>>>>>> bf2b19ff3eb34f6b0a16c2598f3b9d49efd77191
        if weight and ('.' not in weight):
            weight = int(weight)*1.0
        if cost and ('.' not in cost):
            cost = int(cost)*1.0
        """if expense and ('.' not in expense):
            expense = int(expense)*1.0
        else:
            expense = 0.0"""
        if weight and cost:
            weight = float(weight)
            cost = float(cost)
            total_cost = float(weight)*float(cost)

        if Trip.objects.all().filter(truck=truck, trip_complete=False).exists():
            msg = "The truck with truck number:"+truck+" has not completed it's previous trip. Please update the details if required."
            context = {"msg":msg}
            return render(request, "new.html", context)
        #save the data
        t = Trip(truck=truck, trip_start_date=trip_start_date, trip_start_time=trip_start_time, source=source, destination=destination, driver=driver, item=item, consignee=consignee, weight=weight, cost_per_ton=cost, total_cost=total_cost)
        t.save()
        msg = "Your new trip has been created"
        context = {"msg":msg}
        return render(request,"new.html",context)
    else:
        return render(request,"new.html")

@login_required
def update_trip(request):
    exp = 0.00
    comm = ""
    if request.method == "POST":
        truck = request.POST.get("truck").upper()
        #expense = request.POST.get("expense")
        #comment = request.POST.get("comment")
        trip_end_date = request.POST.get("trip_end_date")
        trip_end_time = request.POST.get("trip_end_time")
        if not Trip.objects.filter(truck=truck, trip_complete=False).exists():
            msg = "The truck with number:"+truck+" is not taking any trip right now."
            context = {"msg":msg}
            return render(request,"update.html",context)
        t = Trip.objects.filter(truck=truck, trip_complete=False)
        """if expense and ('.' not in expense):
            expense = int(expense)*1.0
            exp = t[0].expense+float(expense)
        if comment:
            comm = t[0].comment+'\n'+comment
            Trip.objects.filter(truck=truck, trip_complete=False).update(expense=exp, comment=comm)"""
        if trip_end_date:
            if trip_end_time:
                Trip.objects.filter(truck=truck, trip_complete=False).update(trip_end_date=trip_end_date, trip_end_time=trip_end_time, trip_complete = True)
            else:
                Trip.objects.filter(truck=truck, trip_complete=False).update(trip_end_date=trip_end_date, trip_complete = True)
        msg = "Trip details updated"
        context = {"msg":msg}
        return render(request,"update.html",context)
    else:
        return render(request,"update.html")

@login_required
def expenses(request):
    expense = 0.0
    if request.method == "POST":
        truck = request.POST.get("truck").upper()
        expense = request.POST.get("expense")
        if expense and ('.' not in expense):
            expense = int(expense)*1.0
        else:
            expense = float(expense)
        comment = request.POST.get("comment")
        expense_date = request.POST.get("expense_date")
        print(expense_date)
        t = Expenses(truck=truck, expense=expense, comment=comment, expense_date=expense_date)
        t.save()
        msg = "Expense saved successfully!"
        context = {"msg":msg}
        return render(request, "expenses.html", context)
    else:
        return render(request,"expenses.html")