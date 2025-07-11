# content/serializers.py

from rest_framework import serializers
from .models import LevelZone, Topic, ReadingContent, PDF

class LevelZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelZone
        fields = ['id', 'title', 'description', 'created_at']

class TopicSerializer(serializers.ModelSerializer):
    zone = LevelZoneSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'zone', 'name', 'description', 'tags']

class ReadingContentSerializer(serializers.ModelSerializer):
    level = LevelZoneSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = ReadingContent
        fields = ['id', 'level', 'topic', 'title', 'body', 'created_at']

class PDFSerializer(serializers.ModelSerializer):
    level = LevelZoneSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = PDF
        fields = ['id', 'uploaded_by', 'level', 'topic', 'title', 'file_path', 'status', 'created_at']
