from django.urls import path,re_path
# from .views import CPULoadView
from .views import CPULoadPageView,CPULoadAPIView,latest_cpu_load

app_name = 'cpu'

urlpatterns = [
    path('cpu/load/', CPULoadAPIView.as_view(), name='cpu_load_api'),
    # path('', CPULoadView.as_view(), name='cpu_load_page'),
    path('', CPULoadPageView, name='cpu_load_page'),
    path('api/latest_data/', latest_cpu_load, name='latest_cpu_load'),

]