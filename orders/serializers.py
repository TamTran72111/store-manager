from rest_framework import serializers

from .models import Order, OrderDetail


class OrderDetailBaseSerializer(serializers.ModelSerializer):
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


class OrderDetailSerializer(OrderDetailBaseSerializer):
    def validate_quantity(self, attr):
        if attr <= 0:
            raise serializers.ValidationError(
                'The quantity must be greater than 0')
        return attr

    def create(self, validated_data):
        price = validated_data.get('price', 0)
        if price <= 0:
            validated_data['price'] = validated_data['unit'].price
        return super().create(validated_data)


class UpdatePriceSerializer(OrderDetailBaseSerializer):
    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'unit', 'product_id', 'product_name',
                  'unit_name', 'price', 'cost', 'ready', 'quantity', )

        extra_kwargs = {
            'order': {'read_only': True},
            'unit': {'read_only': True},
            'price': {'read_only': True},
            'ready': {'read_only': True},
            'quantity': {'read_only': True},
        }

    def update(self, instance, validated_data):
        instance.price = instance.unit.price
        return super().update(instance, validated_data)


class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
        source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_name', 'status',
                  'created_at', 'debt', 'subtotal')


class OrderRetrieveSerializer(OrderSerializer):
    details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_name', 'status',
                  'created_at', 'subtotal', 'debt', 'details')
