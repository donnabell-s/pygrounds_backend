from django.db import models
from users.models import StudentProfile

class SystemEvent(models.Model):
    student = models.ForeignKey(StudentProfile, null=True, on_delete=models.SET_NULL)
    event_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
