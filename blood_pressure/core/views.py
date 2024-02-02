from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import DeleteView, UpdateView
from .models import BloodPressure
from .forms import BloodPressureForm
from django.db.models import Avg, Q
from datetime import datetime
from django.utils.timezone import make_aware
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from .utils import get_plot
import pandas as pd

class Index(View):
    def get(self, request):
        form = BloodPressureForm()
        data = BloodPressure.objects.order_by("-timestamp")
        data_len = len(data)

        #conditional plotting
        if data_len >= 7:
            df = pd.DataFrame.from_records(data.values("timestamp", "systolic", "diastolic", "hearth_rate"))
            chart = get_plot(df.index, df["systolic"], df["diastolic"], df["hearth_rate"])
        else:
            chart = False

        #pagination
        # paginator = Paginator(data, 7)
        # page_number = request.GET.get("page")
        # page_obj = paginator.get_page(page_number)

        avg_systolic = data.aggregate(Avg("systolic"))["systolic__avg"]
        avg_diastolic = data.aggregate(Avg("diastolic"))["diastolic__avg"]
        avg_hearth_rate = data.aggregate(Avg("hearth_rate"))["hearth_rate__avg"]

        context = {"form": form,
                   "data": data,
                   "data_len": data_len,
                   "avg_sys":avg_systolic, 
                   "avg_dia":avg_diastolic, 
                   "avg_hr":avg_hearth_rate,
                   "chart":chart}

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
        
        data = BloodPressure.objects.filter(Q(timestamp__range=[make_aware(start_date), make_aware(end_date)])).order_by("-timestamp")
        if len(data) == 0:
            avg_systolic, avg_diastolic, avg_hearth_rate = "---"
        else:
            avg_systolic = data.aggregate(Avg("systolic"))["systolic__avg"]
            avg_diastolic = data.aggregate(Avg("diastolic"))["diastolic__avg"]
            avg_hearth_rate = data.aggregate(Avg("hearth_rate"))["hearth_rate__avg"]

        return render(request, "filtered_index.html", {"start_date":start_date,"end_date":end_date,"data":data, "avg_sys":avg_systolic, "avg_dia":avg_diastolic, "avg_hr":avg_hearth_rate})

class DeleteItem(DeleteView):
    model = BloodPressure

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        if "filter" in referer:
            #return reverse("core:filteredIndex")
            return reverse("core:index")
        else:
            return reverse("core:index")
            
class EditItem(UpdateView):
    model = BloodPressure
    form_class = BloodPressureForm

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(BloodPressure, pk=self.kwargs['pk'])
        return obj

    def get_success_url(self):
        path = self.request.path
        if "filter" in path:
            return reverse("core:filteredIndex")
        else:
            return reverse("core:index")