from django.db import models
from users.models import StudentProfile
from content.models import LevelZone
from questions.models import Question

class Minigame(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    instructions = models.TextField()
    is_initial = models.BooleanField(default=False)

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
