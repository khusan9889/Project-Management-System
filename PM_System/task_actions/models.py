from django.db import models
from tasks.models import Task

# Create your models here.

class Task_action(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
