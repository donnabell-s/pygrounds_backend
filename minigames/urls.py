from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (MinigameViewSet, AssessmentViewSet, AssessmentItemViewSet, AssessmentItemResultViewSet)

router = DefaultRouter()
router.register(r'minigames', MinigameViewSet)
router.register(r'assessments', AssessmentViewSet)
router.register(r'assessment-items', AssessmentItemViewSet)
router.register(r'assessment-results', AssessmentItemResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
