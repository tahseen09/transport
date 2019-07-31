from django.db import models

class Trip(models.Model):
    truck = models.CharField(blank=True, null=True, max_length=100)
    trip_start_date = models.DateField(blank=True, null=True)
    #trip_start_time = models.TimeField(blank=True, null=True)
    trip_end_date = models.DateField(blank=True, null=True)
    #trip_end_time = models.TimeField(blank=True, null=True)
    source = models.CharField(max_length = 100, blank = True, null=True)
    #consignee = models.CharField(max_length = 100, blank = True, null=True)
    destination = models.CharField(max_length = 100, blank = True, null=True)
    #driver = models.CharField(max_length = 30, blank = False, null=True)
    #item = models.CharField(max_length = 30, blank = False, null=True)
    #trip_complete = models.BooleanField(default=False)
    total_weight = models.FloatField(blank=True, null=True)
    rec_weight = models.FloatField(blank=True, null=True)
    cost_per_ton = models.FloatField(blank=True, null=True)
    shortage = models.FloatField(blank=True, null=True)
    status = models.CharField(blank=True, max_length=100)
    mop = models.CharField(blank=True, max_length=30)
    #diesel = models.FloatField(blank=True, null=True, default=0.0)
    total_cost = models.FloatField(blank=True, null=True)
    tp_pass = models.CharField(blank=True, max_length=100)
    sl_no = models.CharField(blank=True, null=True,max_length=100)
    
    
    class Meta:
        unique_together = ["truck","trip_start_date", "sl_no"]

    def __str__(self):
        show = str(self.truck)+'|'+str(self.trip_start_date)+'|'+str(self.sl_no)
        return show

class Expenses(models.Model):
    truck = models.CharField(blank=False, null=False, max_length = 40)
    comment = models.TextField(blank=True, null=True)
    expense = models.FloatField(default=0.00, blank=True, null=True)
    expense_date = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ["truck", "expense_date", "comment", "expense"]
    
    def __str__(self):
        show = str(self.truck)+'|'+str(self.expense_date)
        return show
