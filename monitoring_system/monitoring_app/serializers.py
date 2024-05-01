from rest_framework import serializers
from .models import CPULoad

class CPULoadSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = CPULoad
        fields = ['timestamp', 'load_percentage']
