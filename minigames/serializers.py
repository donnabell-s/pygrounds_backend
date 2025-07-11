from rest_framework import serializers
from .models import Minigame, Assessment, AssessmentItem, AssessmentItemResult

class MinigameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minigame
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class AssessmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentItem
        fields = '__all__'

class AssessmentItemResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentItemResult
        fields = '__all__'
