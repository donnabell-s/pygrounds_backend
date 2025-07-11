from django.db import models
from users.models import StudentProfile
from content.models import LevelZone
from questions.models import Question

from django.db import models

class Minigame(models.Model):
    name = models.CharField(max_length=100)

    short_description = models.CharField(max_length=255, blank=True, null=True)  
    type = models.CharField(max_length=50)
    instructions = models.JSONField(default=list, blank=True)
    tips = models.JSONField(default=list, blank=True)
    is_initial = models.BooleanField(default=False)
    challenges = models.IntegerField(default=1, null=True, blank=True)
    lives = models.IntegerField(default=1, null=True, blank=True)
    time_limit_seconds = models.IntegerField(null=True, blank=True, help_text="Seconds (null = no time limit)")


class Assessment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    level = models.ForeignKey(LevelZone, on_delete=models.SET_NULL, null=True)
    minigame = models.ForeignKey(Minigame, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

class AssessmentItem(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    served_at = models.DateTimeField(auto_now_add=True)

class AssessmentItemResult(models.Model):
    item = models.OneToOneField(AssessmentItem, on_delete=models.CASCADE)
    user_answer = models.TextField()
    is_correct = models.BooleanField()
    score = models.FloatField()
