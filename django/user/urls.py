from user.views import UserViewSet
from rest_framework.routers import SimpleRouter


urlpatterns = []

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls
