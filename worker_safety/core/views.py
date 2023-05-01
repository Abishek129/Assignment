from django.shortcuts import render


from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import generics
from .models import Worker
from .serializers import WorkerSerializer

class WorkerList(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer




