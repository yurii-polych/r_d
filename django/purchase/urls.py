from django.urls import path
from purchase.views import PurchaseListView, PurchaseDetailView, PurchaseCreateView


urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase-list'),
    path('detail/<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('create', PurchaseCreateView.as_view(), name='purchase-create'),
]
