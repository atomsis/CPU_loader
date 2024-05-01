from rest_framework import serializers
from .models import CPULoad

class CPULoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPULoad
        fields = '__all__'
