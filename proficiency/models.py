from django.db import models
from users.models import StudentProfile
from content.models import Topic
from minigames.models import Assessment

class TopicProficiency(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    proficiency_score = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

class ScoreLog(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    average_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
