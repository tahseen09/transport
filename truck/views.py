from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Trip, Expenses


def index(request):
    return HttpResponse("Welcome to Transport Management")

@login_required
def dashboard(request):
    road = None
    total_sale = 0.0
    total_expense = 0.0
    total_weight = 0.0
    total_rec_weight = 0.0
    total_shortage = 0.0
    if request.method == "POST":
        start_date = request.POST.get("startdate")
        end_date = request.POST.get("enddate")
        truck = request.POST.get("truck").upper()

        if not (start_date or end_date or truck):
            today = datetime.now().strftime('%Y-%m-%d')
            road = Trip.objects.all().filter(trip_start_date = today )
            expenses = Expenses.objects.all().filter(expense_date = today)
            for r in road:
                total_sale = total_sale+r.total_cost
            for e in expenses:
                total_expense = total_expense+e.expense
            context = {"road":road, "expenses":expenses, "total_sale":total_sale, "total_expense": total_expense}
            return render(request, "dashboard.html", context)

        if start_date and end_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__gte = start_date, trip_start_date__lte = end_date, truck = truck)
                expenses = Expenses.objects.all().filter(expense_date__gte = start_date, expense_date__lte = end_date, truck = truck)
                for r in road:
                    total_sale = total_sale+r.total_cost
                    total_weight = total_weight+r.total_weight
                    total_rec_weight = total_rec_weight+r.rec_weight
                    total_shortage = total_shortage+r.shortage
                for e in expenses:
                    total_expense = total_expense+e.expense
                profit = total_sale-total_expense

                context = {"road":road, "total_sale":total_sale, "expenses":expenses, "total_expense":total_expense,"total_weight":total_weight, "total_rec_weight":total_rec_weight,"total_shortage":total_shortage, "profit":profit}
                return render(request, "detail.html", context)
            else:
                road = Trip.objects.all().filter(trip_start_date__gte = start_date, trip_start_date__lte = end_date)
                expenses = Expenses.objects.all().filter(expense_date__gte = start_date, expense_date__lte = end_date)

        elif start_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__gte=start_date, truck=truck)
                expenses = Expenses.objects.all().filter(expense_date__gte = start_date, truck = truck)
            else:
                road = Trip.objects.all().filter(trip_start_date__gte=start_date)
                expenses = Expenses.objects.all().filter(expense_date__gte = start_date)

        elif end_date:
            if truck:
                road = Trip.objects.all().filter(trip_start_date__lte=end_date, truck=truck)
                expenses = Expenses.objects.all().filter(expense_date__lte=end_date, truck=truck)
            else:
                road = Trip.objects.all().filter(trip_start_date__lte=end_date)
                expenses = Expenses.objects.all().filter(expense_date__lte=end_date)

        else:
            road = Trip.objects.all().filter(truck=truck).sort('truck')
            expenses = Expenses.objects.all().filter(truck = truck)

        for r in road:
            total_sale = total_sale+r.total_cost
            total_weight = total_weight+r.total_weight
            total_rec_weight = total_rec_weight+r.rec_weight
            total_shortage = total_shortage+r.shortage
        for e in expenses:
            total_expense = total_expense+e.expense
        profit = total_sale-total_expense
        context = {"road": road, "expenses": expenses, "truck": truck, "start_date": start_date, "end_date": end_date, "total_sale": total_sale,
                   "total_expense": total_expense, "total_weight": total_weight, "total_rec_weight": total_rec_weight, "total_shortage": total_shortage, "profit": profit}
        return render(request,"dashboard.html",context)

    else:
        today = datetime.now().strftime('%Y-%m-%d')
        road = Trip.objects.all().filter(trip_start_date = today )
        expenses = Expenses.objects.all().filter(expense_date = today)
        for r in road:
            total_sale = total_sale+r.total_cost
            total_weight = total_weight+r.total_weight
            total_rec_weight = total_rec_weight+r.rec_weight
            total_shortage = total_shortage+r.shortage
        for e in expenses:
            total_expense = total_expense+e.expense
        profit = total_sale-total_expense
        context = {"road": road, "expenses": expenses, "total_sale": total_sale, "total_weight": total_weight,
                   "total_rec_weight": total_rec_weight, "total_shortage": total_shortage, "total_expense": total_expense, "profit": profit}
        return render(request, "dashboard.html", context)

@login_required
def new_trip(request):
    advance=0.0
    diesel=0.0
    less=0.0
    if request.method == "POST":
        truck = request.POST.get("truck").upper()
        trip_start_date = request.POST.get("trip_start_date")
        source = request.POST.get("source").upper()
        destination = request.POST.get("destination").upper()
        total_weight = request.POST.get("total_weight")
        cost = request.POST.get("cost")
        rec_weight = request.POST.get("rec_weight")
        mop = request.POST.get("mop").upper()
        shortage = request.POST.get("shortage")
        less = request.POST.get("less")
        status = request.POST.get("status").upper()
        diesel = request.POST.get("diesel")
        advance = request.POST.get("advance")
        sl_no = request.POST.get("sl_no")
        tp_pass = request.POST.get("pass").upper()

        if total_weight and ('.' not in total_weight):
            total_weight = int(total_weight)*1.0
        if advance and ('.' not in advance):
            advance = int(advance)*1.0
        if cost and ('.' not in cost):
            cost = int(cost)*1.0
        if shortage and ('.' not in shortage):
            shortage = int(shortage)*1.0
        if less and ('.' not in less):
            less = int(less)*1.0
        if rec_weight and ('.' not in rec_weight):
            rec_weight = int(rec_weight)*1.0
        if diesel and ('.' not in diesel):
            diesel = int(diesel)*1.0

        total_cost = (float(rec_weight)*float(cost))
        #save the data
        t = Trip(truck=truck, trip_start_date=trip_start_date, source=source, destination=destination, total_weight=total_weight, cost_per_ton=cost, total_cost=total_cost, rec_weight=rec_weight, shortage=shortage, sl_no=sl_no, tp_pass=tp_pass, status=status, mop=mop)
        t.save()
        if diesel>0.0:
            e = Expenses(expense=diesel, comment="Diesel", expense_date=trip_start_date, truck=truck)
            e.save()
        if less>0.0:
            e = Expenses(expense=less, comment="Less", expense_date=trip_start_date, truck=truck)
            e.save()
        if float(advance)>0.0:
            e = Expenses(expense=advance, comment="Driver Advance", expense_date=trip_start_date, truck=truck)
            e.save()
        expense = diesel+advance+less
        profit = total_cost-expense

        msg = "Your new trip has been created"
        trip_start_date = trip_start_date[8:]+'/'+trip_start_date[5:7]+'/'+trip_start_date[0:4]
        context = {"msg":msg,"truck":truck, "sl_no":sl_no, "trip_start_date":trip_start_date, "source":source, "destination":destination, "total_weight":total_weight, "cost":cost, "rec_weight":rec_weight, "tp_pass":tp_pass, "shortage":shortage, "less":less, "status":status, "diesel":diesel, "advance":advance, "mop":mop, "total_cost":total_cost, "profit":profit, "expense":expense}
        return render(request,"print.html",context)
    else:
        return render(request,"new.html")

@login_required
def update_trip(request):
    exp = 0.00
    comm = ""
    if request.method == "POST":
        sl_no = request.POST.get("sl_no")
        t = Trip.objects.filter(sl_no=sl_no)
        trip_end_date = request.POST.get("trip_end_date")
        if not t:
            msg = "Trip with Serial number:"+sl_no+" doesn't exist"
            context = {"msg":msg}
            return render(request,"update.html",context)

        if trip_end_date:
            t.update(trip_end_date=trip_end_date)
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
        t = Expenses(truck=truck, expense=expense, comment=comment, expense_date=expense_date)
        t.save()
        msg = "Expense saved successfully!"
        context = {"msg":msg}
        return render(request, "expenses.html", context)
    else:
        return render(request,"expenses.html")