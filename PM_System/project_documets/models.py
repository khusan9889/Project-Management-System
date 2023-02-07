from django.db import models
from projects.models import Project
# Create your models here.

class Project_document(models.Model): 
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    description = models.TextField()

    def __str__(self):
        return self.name