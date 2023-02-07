from django.db import models
from users.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lead_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=255)
    dete_start = models.DateField()
    date_end = models.DateField()
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
    