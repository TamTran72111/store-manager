from rest_framework.viewsets import ModelViewSet

from .models import Customer
from .serializers import CustomerSerialzier


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerialzier

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        return Customer.search(name)
