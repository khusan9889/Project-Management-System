from django.db import models
from projects.models import Project
from task_statuses.models import Task_status

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    order_number = models.IntegerField()
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    status_id = models.ForeignKey(Task_status, on_delete=models.SET_NULL, null=True, blank=True)

