from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet

router = DefaultRouter()
router.register(r"cats", CatViewSet, basename="cat")
urlpatterns = router.urls
