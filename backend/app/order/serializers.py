from rest_framework import  serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    orderID = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderID(self, obj):
        return obj.orderID