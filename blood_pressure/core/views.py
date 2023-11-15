from django.shortcuts import render
from django.views.generic import View
from .models import BloodPressure
from .forms import BloodPressureForm
from django.db.models import Avg, Q
from datetime import datetime
from django.utils.timezone import make_aware
from django.http import HttpResponseRedirect
from django.contrib import messages

class Index(View):

    def get(self, request):
        form = BloodPressureForm()
        data = BloodPressure.objects.order_by("-timestamp")
        avg_systolic = data.aggregate(Avg("systolic"))["systolic__avg"]
        avg_diastolic = data.aggregate(Avg("diastolic"))["diastolic__avg"]
        avg_hearth_rate = data.aggregate(Avg("hearth_rate"))["hearth_rate__avg"]

        context = {"form": form,
                   "data": data, 
                   "avg_sys":avg_systolic, 
                   "avg_dia":avg_diastolic, 
                   "avg_hr":avg_hearth_rate}

        return render(request, "index.html", context)
    
    def post(self, request):
        form = BloodPressureForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
        else:
            messages.info(request, "Coś poszło nie tak, spróbuj ponownie!") 
            return HttpResponseRedirect(request.path)

        
    
class FilteredIndex(View):
    def post(self, request):
        start_date, end_date = datetime.strptime(request.POST.get("start_date"), '%Y-%m-%d').date(), datetime.strptime(request.POST.get("end_date"), '%Y-%m-%d').date()
        start_date, end_date = datetime.combine(start_date, datetime.min.time()), datetime.combine(end_date, datetime.max.time())
        
        data = BloodPressure.objects.filter(Q(timestamp__range=[make_aware(start_date), make_aware(end_date)]))
        if len(data) == 0:
            avg_systolic, avg_diastolic, avg_hearth_rate = "---"
        else:
            avg_systolic = data.aggregate(Avg("systolic"))["systolic__avg"]
            avg_diastolic = data.aggregate(Avg("diastolic"))["diastolic__avg"]
            avg_hearth_rate = data.aggregate(Avg("hearth_rate"))["hearth_rate__avg"]

        return render(request, "filtered_index.html", {"start_date":start_date,"end_date":end_date,"data":data, "avg_sys":avg_systolic, "avg_dia":avg_diastolic, "avg_hr":avg_hearth_rate})



