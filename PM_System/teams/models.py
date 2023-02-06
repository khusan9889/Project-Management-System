from django.db import models
from users.models import User
# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=255)
    lead_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
