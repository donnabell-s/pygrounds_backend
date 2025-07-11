from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)