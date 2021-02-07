from rest_framework.viewsets import ModelViewSet

from .models import Customer
from .serializers import CustomerSerialzier


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerialzier
    queryset = Customer.objects.all()
