from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, UnitCreateAPIView, UnitAPIView

router = DefaultRouter()
router.register('', ProductViewSet, basename='product')

urlpatterns = [
    path('products/', include(router.urls)),
    path('units/', UnitCreateAPIView.as_view()),
    path('units/<int:pk>/', UnitAPIView.as_view()),
]
