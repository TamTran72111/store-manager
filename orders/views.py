from rest_framework import mixins
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import GenericViewSet

from .models import Order, OrderDetail
from .serializers import (
    OrderSerializer,
    OrderRetrieveSerializer,
    OrderDetailSerializer,
    UpdatePriceSerializer)


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    def get_queryset(self):
        query = self.request.query_params
        return Order.get_query_orders(query)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderRetrieveSerializer
        return OrderSerializer


class OrderDetailViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()


class UpdatePriceAPIView(UpdateAPIView):
    serializer_class = UpdatePriceSerializer
    queryset = OrderDetail.objects.all()
