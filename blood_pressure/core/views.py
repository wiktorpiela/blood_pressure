from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BloodPressure
from django.db.models import Avg

class Index(TemplateView):
    blood = BloodPressure
    data = blood.objects.all()
    avg_systolic = blood.objects.aggregate(Avg("systolic"))["systolic__avg"]
    avg_diastolic = blood.objects.aggregate(Avg("diastolic"))["diastolic__avg"]
    avg_hearth_rate = blood.objects.aggregate(Avg("hearth_rate"))["hearth_rate__avg"]
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(Index, self).get_context_data(**kwargs)
        context.update({"data": self.data, "len":len(self.data), "avg_sys":self.avg_systolic, "avg_dia":self.avg_diastolic, "avg_hr":self.avg_hearth_rate})
        return context
