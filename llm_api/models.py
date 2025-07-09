from django.db import models
from users.models import StudentProfile
from content.models import Topic

class LLMLog(models.Model):
    student = models.ForeignKey(StudentProfile, null=True, on_delete=models.SET_NULL)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    generation_type = models.CharField(max_length=20, choices=[
        ('question', 'Question'),
        ('hint', 'Hint'),
        ('explanation', 'Explanation'),
    ])
    prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
