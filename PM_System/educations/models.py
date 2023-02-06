from django.db import models
from users.models import User
# Create your models here.

class Education(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    university = models.CharField(max_length=255)
    university_address = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    from_date = models.DateField()
    till_date = models.DateField()