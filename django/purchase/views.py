from purchase.models import Purchase

from rest_framework.viewsets import ModelViewSet
from purchase.serializers import PurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
