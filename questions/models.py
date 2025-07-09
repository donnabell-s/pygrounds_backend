from django.db import models
from content.models import Topic

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=20)  # MCQ, TF, FITB, etc.
    difficulty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
