from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentProfileViewSet, AdminProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentProfileViewSet)
router.register(r'admins', AdminProfileViewSet)

urlpatterns = router.urls
