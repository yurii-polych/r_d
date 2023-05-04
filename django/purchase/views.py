from purchase.models import Purchase

from rest_framework.viewsets import ModelViewSet
from purchase.serializers import PurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.get_queryset().order_by('id')
    serializer_class = PurchaseSerializer
    filterset_fields = '__all__'
