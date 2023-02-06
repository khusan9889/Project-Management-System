from django.db import models

# Create your models here.

class Task_status(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

