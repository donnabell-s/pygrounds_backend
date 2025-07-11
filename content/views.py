# content/views.py

from rest_framework import viewsets
from .models import LevelZone, Topic, ReadingContent, PDF
from .serializers import LevelZoneSerializer, TopicSerializer, ReadingContentSerializer, PDFSerializer

class LevelZoneViewSet(viewsets.ModelViewSet):
    queryset = LevelZone.objects.all()
    serializer_class = LevelZoneSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class ReadingContentViewSet(viewsets.ModelViewSet):
    queryset = ReadingContent.objects.all()
    serializer_class = ReadingContentSerializer

class PDFViewSet(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
