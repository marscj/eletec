from rest_framework import  serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    job = serializers.StringRelatedField(read_only=True, many=True)
    
    user_id = serializers.IntegerField()

    orderID = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderID(self, obj):
        return obj.orderID