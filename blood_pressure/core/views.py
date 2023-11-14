from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BloodPressure

class Index(TemplateView):
    data = BloodPressure.objects.all()
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(Index, self).get_context_data(**kwargs)
        context.update({"data": self.data, "len":len(self.data)})
        return context
