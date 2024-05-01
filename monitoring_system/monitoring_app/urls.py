from django.urls import path,re_path
# from .views import CPULoadView
from .views import CPULoadPageView,CPULoadAPIView,get_last_100_cpu_load

app_name = 'cpu'

urlpatterns = [
    path('cpu/load/', CPULoadAPIView.as_view(), name='cpu_load_api'),
    # path('', CPULoadView.as_view(), name='cpu_load_page'),
    path('', CPULoadPageView, name='cpu_load_page'),
    path('get_last_100_cpu_load/',get_last_100_cpu_load)

]