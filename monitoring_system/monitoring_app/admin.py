from django.contrib import admin
from .models import CPULoad

class CPULoadAdmin(admin.ModelAdmin):
    fields = ('load_percentage',)

admin.site.register(CPULoad, CPULoadAdmin)
