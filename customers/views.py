from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Customer
from .serializers import CustomerSerialzier


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = CustomerSerialzier

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        return Customer.search(name)
