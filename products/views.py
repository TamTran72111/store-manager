from rest_framework import mixins
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.viewsets import GenericViewSet

from .models import Product, Unit
from .serializers import (
    ProductSerializer,
    UnitSerializer,
    UnitCreateSerializer
)


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        return Product.search(name)


class UnitCreateAPIView(CreateAPIView):
    serializer_class = UnitCreateSerializer
    queryset = Unit.objects.all()


class UnitAPIView(RetrieveUpdateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
