from django import forms
from .models import BloodPressure

class BloodPressureForm(forms.ModelForm):
    class Meta:
        model = BloodPressure
        exclude = ("timestamp", )