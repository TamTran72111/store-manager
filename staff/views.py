from rest_framework import viewsets, mixins

from .models import Staff
from .serializers import StaffSerializer, StaffCreateSerializer


class StaffViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Staff.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return StaffCreateSerializer
        return StaffSerializer
