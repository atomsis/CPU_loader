from django.db import models
from datetime import timedelta


class CPULoad(models.Model):
    load_percentage = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True,)

    class Meta:
        get_latest_by = 'timestamp'

    def __str__(self):
        return f'CPU={self.load_percentage},TIME={self.formatted_timestamp()}'

    def formatted_timestamp(self):
        corrected_time = self.timestamp + timedelta(hours=3)
        return corrected_time.strftime('%Y-%m-%d %H:%M:%S')
