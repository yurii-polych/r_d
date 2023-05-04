from purchase.views import PurchaseViewSet

from rest_framework.routers import SimpleRouter


urlpatterns = []

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls
