from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, OrderDetailViewSet, UpdatePriceAPIView, PaymentViewSet

router = DefaultRouter()

router.register('details', OrderDetailViewSet, basename='order-detail')
router.register('payments', PaymentViewSet, basename='order-payments')
router.register('', OrderViewSet, basename='order')


urlpatterns = [
    path(
        'orders/details/<int:pk>/update-price/',
        UpdatePriceAPIView.as_view()
    ),
    path('orders/', include(router.urls))
]
