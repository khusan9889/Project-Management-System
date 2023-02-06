from django.db import models
from projects.models import Project
from resumes.models import Resume

# Create your models here.
class Resume_project(models.Model):
    resume_id = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True)
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)