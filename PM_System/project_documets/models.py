from django.db import models
from projects.models import Project
# Create your models here.

class Project_document(models.Model): 
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    description = models.TextField()
