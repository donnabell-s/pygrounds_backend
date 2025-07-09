from django.db import models
from users.models import StudentProfile

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    xp_reward = models.IntegerField()

class UserAchievement(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date_earned = models.DateTimeField(auto_now_add=True)
