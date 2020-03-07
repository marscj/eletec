from rest_framework import  serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Order
from app.user.serializers import UserSerializer, ContractSerializer, CommentSerializer
from app.job.serializers import JobSerializer
from app.generic.serializers import ImageSerializer

class OrderSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    job = JobSerializer(read_only=True, many=True)

    contract = ContractSerializer(read_only=True)

    images = ImageSerializer(read_only=True, many=True)

    comments = CommentSerializer(read_only=True, many=True)

    contract_id = serializers.IntegerField()
    
    user_id = serializers.IntegerField()

    orderID = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderID(self, obj):
        return obj.orderID