from django.db import models
from users.models import User
# Create your models here.


class Resume(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resume_files/', blank=True)
