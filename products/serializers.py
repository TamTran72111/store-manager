from rest_framework import serializers

from .models import Product, Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name', 'price')


class UnitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('product', 'name', 'price')


class ProductSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'units')