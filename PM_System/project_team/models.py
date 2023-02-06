from django.db import models
from teams.models import Team
from projects.models import Project
# Create your models here.


class Project_team(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
