from django.db import models
from tasks.models import Task
from users.models import User

# Create your models here.

class Task_user(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
