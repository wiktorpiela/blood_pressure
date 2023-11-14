from django.db import models

class BloodPressure(models.Model):
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    hearth_rate = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.timestamp}"
