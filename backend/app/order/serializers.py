from rest_framework import  serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Order
from app.user.serializers import UserSerializer, ContractSerializer, CommentSerializer
from app.job.serializers import JobSerializer
from app.generic.serializers import ImageSerializer

class OrderSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    user_id = serializers.IntegerField()

    contract = ContractSerializer(read_only=True)

    contract_id = serializers.IntegerField(required=False, allow_null=True)
    
    orderID = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderID(self, obj):
        return obj.orderID