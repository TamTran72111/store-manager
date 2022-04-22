from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Customer
from .serializers import CustomerCreateSerialzier, CustomerSerialzier


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return CustomerCreateSerialzier
        return CustomerSerialzier

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        return Customer.search(name)
