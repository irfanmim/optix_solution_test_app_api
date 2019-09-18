from django.shortcuts import render
from rest_framework import viewsets
from .models import Machine, Job, Task, TaskQueue
from .serializers import MachineSerializer, JobSerializer, TaskSerializer, TaskQueueSerializer

# Create your views here.
class MachineView(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer 

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskQueueView(viewsets.ModelViewSet):
    queryset = TaskQueue.objects.all()
    serializer_class = TaskQueueSerializer