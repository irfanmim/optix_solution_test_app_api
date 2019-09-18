from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/machines', views.MachineView, basename="machines")
router.register('api/jobs', views.JobView, basename="jobs")
router.register('api/tasks', views.TaskView, basename="tasks")
router.register('api/tasks_queue', views.TaskQueueView)

urlpatterns = [
    path('', include(router.urls)),
]