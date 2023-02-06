from django.db import models

# Create your models here.

class Position(models.Model):
    name  = models.CharField(max_length=255)