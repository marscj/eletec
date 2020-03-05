from rest_framework import  serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Order
from app.user.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True, many=False)

    job = serializers.StringRelatedField(read_only=True, many=True)
    
    user_id = serializers.IntegerField()

    orderID = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderID(self, obj):
        return obj.orderID