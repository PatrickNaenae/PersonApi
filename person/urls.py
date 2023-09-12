from rest_framework import routers
from .views import PersonViewSet

router = routers.DefaultRouter()
router.register(r'api', PersonViewSet, basename='person')

urlpatterns = router.urls
