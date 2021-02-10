from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        query = self.request.query_params
        return Order.get_query_orders(query)


class OrderDetailViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
