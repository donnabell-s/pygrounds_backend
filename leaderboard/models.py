from django.db import models
from users.models import StudentProfile
from minigames.models import Minigame

class LeaderboardEntry(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    minigame = models.ForeignKey(Minigame, null=True, blank=True, on_delete=models.CASCADE)  # null = overall
    xp = models.IntegerField(default=0)
    total_completed = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
