from rest_framework import serializers

from .models import Order, OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    unit_name = serializers.SerializerMethodField()

    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'unit', 'product_id', 'product_name',
                  'unit_name', 'price', 'discount', 'cost', 'ready',
                  'quantity', )

    def get_product_id(self, instance):
        return instance.product.id

    def get_product_name(self, instance):
        return instance.product.name

    def get_unit_name(self, instance):
        return instance.unit.name


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    customer_name = serializers.CharField(
        source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_name', 'status',
                  'created_at', 'total')

    def get_total(self, instance):
        return instance.total


class OrderRetrieveSerializer(OrderSerializer):
    details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_name', 'status',
                  'created_at', 'total', 'debt', 'details')
