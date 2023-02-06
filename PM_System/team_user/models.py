from django.db import models
from teams.models import Team
from users.models import User
# Create your models here.

class Team_user(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
