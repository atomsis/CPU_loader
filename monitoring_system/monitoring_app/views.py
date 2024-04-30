import json
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import CPULoad
from .serializers import CPULoadSerializer
from django.shortcuts import render
from django.db.models import Avg, Max, Min
from django.utils import timezone
from django.core import serializers
import requests


@csrf_exempt
def latest_cpu_load(request):
    if request.method == 'GET':
        try:
            latest_record = CPULoad.objects.latest('timestamp')
            data = {
                'timestamp': latest_record.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'load_percentage': latest_record.load_percentage
            }
            return JsonResponse(data)
        except CPULoad.DoesNotExist:
            return JsonResponse({'error': 'No data available'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def CPULoadPageView(request):
    def get_aggregated_data(queryset):
        min_load = round(queryset.aggregate(min_load=Min('load_percentage'))['min_load'], 2)
        max_load = round(queryset.aggregate(max_load=Max('load_percentage'))['max_load'], 2)
        avg_load = round(queryset.aggregate(avg_load=Avg('load_percentage'))['avg_load'], 2)
        return min_load, max_load, avg_load

    # Загрузка последних 100 записей
    last_100_records = CPULoad.objects.order_by('-timestamp')[:100]
    all_records = CPULoad.objects.all()

    min_load_100, max_load_100, avg_load_100 = get_aggregated_data(last_100_records)
    min_load_all, max_load_all, avg_load_all = get_aggregated_data(all_records)
    data = {
        'latest_100': {
            'min_load': min_load_100,
            'max_load': max_load_100,
            'avg_load': avg_load_100
        },
        'all_records': {
            'min_load': min_load_all,
            'max_load': max_load_all,
            'avg_load': avg_load_all
        },
        'last_100_records': last_100_records,
    }
    # Передача данных в шаблон
    return render(request, 'monitoring_app/cpu_load.html', data)



#
class CPULoadAPIView(APIView):
    def post(self, request, format=None):
        serializer = CPULoadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_aggregated_data(self, queryset):
        min_load = round(queryset.aggregate(min_load=Min('load_percentage'))['min_load'], 2)
        max_load = round(queryset.aggregate(max_load=Max('load_percentage'))['max_load'], 2)
        avg_load = round(queryset.aggregate(avg_load=Avg('load_percentage'))['avg_load'], 2)
        return min_load, max_load, avg_load

    def get(self, request, format=None):
        latest_100_records = CPULoad.objects.order_by('-timestamp')[:100]
        all_records = CPULoad.objects.all()

        min_load_100, max_load_100, avg_load_100 = self.get_aggregated_data(latest_100_records)
        min_load_all, max_load_all, avg_load_all = self.get_aggregated_data(all_records)

        data = {
            'latest_100': {
                'min_load': min_load_100,
                'max_load': max_load_100,
                'avg_load': avg_load_100
            },
            'all_records': {
                'min_load': min_load_all,
                'max_load': max_load_all,
                'avg_load': avg_load_all
            }
        }
        return JsonResponse(data)


