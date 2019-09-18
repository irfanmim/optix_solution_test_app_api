from django.db import models

# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=100)
    enabled = models.BooleanField(default=False)
    typeText = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="tasks")
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class TaskQueue(models.Model):
    machine =  models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="tasks_queue")
    task =  models.ForeignKey(Task, on_delete=models.CASCADE, related_name="tasks_queue")
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
