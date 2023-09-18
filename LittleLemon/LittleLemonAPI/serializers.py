from rest_framework import serializers
from .models import MenuItem, Category, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category']


class CartSerializer(serializers.Serializer):
    menuitem = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all())
    quantity = serializers.IntegerField()
    unit_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, read_only=True)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, read_only=True)

    def validate(self, data):
        if data['quantity'] < 1:
            raise serializers.ValidationError(
                'Quantity must be greater than or equal to 1')
        return data


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price']


class OrderSerializer(serializers.Serializer):
    items = OrderItemSerializer(many=True)
    total = serializers.DecimalField(
        max_digits=6, decimal_places=2, read_only=True)
    date = serializers.DateField()

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items:
            OrderItem.objects.create(order=order, **item)
        return order
