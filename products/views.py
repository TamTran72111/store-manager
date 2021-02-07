from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Product, Unit
from .serializers import (
    ProductSerializer,
    UnitSerializer,
    UnitCreateSerializer
)


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class UnitCreateAPIView(CreateAPIView):
    serializer_class = UnitCreateSerializer
    queryset = Unit.objects.all()


class UnitAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
