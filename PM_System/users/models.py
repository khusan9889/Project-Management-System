from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.formfields import PhoneNumberField
from specialities.models import Speciality
from positions.models import Position
from roles.models import Role

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    role_id = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True, blank=True)
    position_id = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = PhoneNumberField()
    secondary_phone = models.CharField(max_length=255, blank=True)


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.username

