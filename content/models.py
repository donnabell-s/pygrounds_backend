from django.db import models

from django.db import models

class LevelZone(models.Model):
    title = models.CharField(max_length=100)  # e.g., "Zone 1: Python Basics"
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Topic(models.Model):
    zone = models.ForeignKey(LevelZone, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=255, blank=True)

class ReadingContent(models.Model):
    level = models.ForeignKey(LevelZone, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PDF(models.Model):
    uploaded_by = models.ForeignKey('users.AdminProfile', on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(LevelZone, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    file_path = models.TextField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
