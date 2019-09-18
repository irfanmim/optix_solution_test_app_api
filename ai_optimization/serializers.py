from rest_framework import serializers
from .models import Machine, Job, Task, TaskQueue

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('__all__')
        
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('__all__')
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')
        
class TaskQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskQueue
        fields = ('__all__')