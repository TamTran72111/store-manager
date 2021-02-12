from rest_framework import serializers

from .models import Order, OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    unit_name = serializers.SerializerMethodField()

    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'unit', 'product_id', 'product_name',
                  'unit_name', 'price', 'cost', 'ready', 'quantity', )

    def get_product_id(self, instance):
        return instance.product.id

    def get_product_name(self, instance):
        return instance.product.name

    def get_unit_name(self, instance):
        return instance.unit.name

    def validate_quantity(self, attr):
        if attr <= 0:
            raise serializers.ValidationError(
                'The quantity must be greater than 0')
        return attr

    def validate(self, attrs):
        price = attrs.get('price', 0)
        if price <= 0:
            attrs['price'] = attrs['unit'].price
        return attrs


class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
        source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_name', 'status',
                  'created_at', 'total')


class OrderRetrieveSerializer(OrderSerializer):
    details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_name', 'status',
                  'created_at', 'total', 'debt', 'details')
