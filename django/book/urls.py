from book.views import BookViewSet
from rest_framework.routers import SimpleRouter


urlpatterns = []

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns += router.urls
