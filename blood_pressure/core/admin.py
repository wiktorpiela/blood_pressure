from django.contrib import admin
from .models import BloodPressure

class BloodPressureTimestamp(admin.ModelAdmin):
    readonly_fields = ("timestamp",)

admin.site.register(BloodPressure, BloodPressureTimestamp)
