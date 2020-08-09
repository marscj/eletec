from rest_framework import  serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Order
from app.user.models import Comment
from app.user.serializers import UserSerializer, ContractSerializer, CommentSerializer
from app.job.serializers import JobSerializer
from app.job.models import Job
from app.generic.serializers import ImageSerializer

from middleware.user import CurrentUserDefault

class OrderSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    user_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))

    contract = ContractSerializer(read_only=True)

    contract_id = serializers.IntegerField(required=False, allow_null=True)
    
    orderID = serializers.SerializerMethodField()

    images = ImageSerializer(required=False, many=True) 

    job = serializers.StringRelatedField(read_only=True, many=True)

    comments = CommentSerializer(required=False, many=True)

    image_count = serializers.IntegerField(
        source='images.count', 
        read_only=True
    )

    job_count = serializers.IntegerField(
        source='job.count', 
        read_only=True
    )

    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderID(self, obj):
        return obj.orderID

    def get_comment_count(self, obj):
        return Comment.objects.filter(object_id=obj.id, content_type__model='order').count()

    def create(self, validated_data):
        # images = validated_data.get('images')
        # print(images)
        print(validated_data)
        order_data = validated_data.pop('images')
        print(order)
        order = Order.objects.create(**validated_data)
        for image in images:
            Images.objects.create(content_type='order', object_id=order.id, **image)

        return order