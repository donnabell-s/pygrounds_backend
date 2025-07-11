# content/urls.py

from rest_framework.routers import DefaultRouter
from .views import LevelZoneViewSet, TopicViewSet, ReadingContentViewSet, PDFViewSet

router = DefaultRouter()
router.register(r'zones', LevelZoneViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'readings', ReadingContentViewSet)
router.register(r'pdfs', PDFViewSet)

urlpatterns = router.urls
