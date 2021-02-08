from rest_framework.viewsets import ModelViewSet


from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        query = self.request.query_params
        return Order.get_query_orders(query)


class OrderDetailViewSet(ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
