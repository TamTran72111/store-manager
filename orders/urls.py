from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, OrderDetailViewSet

router = DefaultRouter()

router.register('details', OrderDetailViewSet, basename='order-detail')
router.register('', OrderViewSet, basename='order')


urlpatterns = [
    path('orders/', include(router.urls))
]
