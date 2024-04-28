from django.urls import path
from .views import CPULoadAPIView,CPULoadPageView

app_name = 'cpu'

urlpatterns = [
    path('cpu/load/', CPULoadAPIView.as_view(), name='cpu_load_api'),
    path('', CPULoadPageView, name='cpu_load_page'),

]
