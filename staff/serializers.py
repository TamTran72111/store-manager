from rest_framework import serializers

from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'name', 'active', 'address', 'phone')
        extra_kwargs = {
            'name': {
                'read_only': True,
            }
        }


class StaffCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'name', 'active', 'address', 'phone')
