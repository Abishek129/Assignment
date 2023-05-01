from django.urls import path
from .views import WorkerList, WorkerDetail

urlpatterns = [
    path('workers/', WorkerList.as_view(), name='worker_list'),
    path('workers/<int:pk>/', WorkerDetail.as_view(), name='worker_detail'),
]
