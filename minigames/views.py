from rest_framework import viewsets
from .models import Minigame, Assessment, AssessmentItem, AssessmentItemResult
from .serializers import (MinigameSerializer, AssessmentSerializer, AssessmentItemSerializer, AssessmentItemResultSerializer)

class MinigameViewSet(viewsets.ModelViewSet):
    queryset = Minigame.objects.all()
    serializer_class = MinigameSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class AssessmentItemViewSet(viewsets.ModelViewSet):
    queryset = AssessmentItem.objects.all()
    serializer_class = AssessmentItemSerializer

class AssessmentItemResultViewSet(viewsets.ModelViewSet):
    queryset = AssessmentItemResult.objects.all()
    serializer_class = AssessmentItemResultSerializer
