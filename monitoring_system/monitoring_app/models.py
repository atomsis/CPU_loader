from django.db import models

class CPULoad(models.Model):
    load_percentage = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)