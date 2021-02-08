from rest_framework.viewsets import ModelViewSet


from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailViewSet(ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
