from django.db import models


class CPULoad(models.Model):
    load_percentage = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def formatted_timestamp(self):
        return self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
