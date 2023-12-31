from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','n_order', 'user', 'products', 'description', 'quantity', 'total_price']
