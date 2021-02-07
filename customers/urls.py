from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet

router = DefaultRouter()
router.register('', CustomerViewSet, basename='customer')

urlpatterns = [
    path('customers/', include(router.urls)),
]
