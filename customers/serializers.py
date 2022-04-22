from rest_framework import serializers

from .models import Customer


class CustomerSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'description', 'phone', 'address', 'debt')
        extra_kwargs = {
            'debt': {
                'read_only': True
            }
        }

class CustomerCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'description', 'phone', 'address', 'debt')