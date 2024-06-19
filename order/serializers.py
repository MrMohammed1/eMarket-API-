from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'name', 'quantity', 'price', 'order']

class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_status', 'payment_status', 'payment_mode', 'city', 'zip_code', 'street', 
                  'country', 'state', 'phone_no', 'total_amount', 'created_at', 'updated_at', 'orderitems']