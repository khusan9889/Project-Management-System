from django.db import models
from users.models import User

# Create your models here.
class Experience(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True)
    company = models.CharField(max_length=255)
    company_address = models.TextField()
    position = models.CharField(max_length=255)
    description = models.TextField()
    from_date = models.DateField()
    till_date = models.DateField()
    