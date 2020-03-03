from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
from django.db.models import Count

from rest_framework import  serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from django.utils import timezone

from .models import User, Address, Skill, WorkTime, Resource, Contract
from app.order.models import Order

class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):

    content_type = ContentTypeSerializer(many=False)

    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    
    permissions = PermissionSerializer(read_only=True, many=True)

    name = serializers.CharField(required=False, max_length=150)
 
    permission = serializers.IntegerField(required=False, write_only=True)
    
    class Meta:
        model = Group
        fields = '__all__'

    def update(self, instance, validated_data):
        permission = validated_data.pop('permission', None)
        if permission is not None:
            if instance.permissions.filter(id=permission).exists():
                instance.permissions.remove(permission)
            else:
                instance.permissions.add(permission)

        return super().update(instance, validated_data)

class UserSerializer(serializers.ModelSerializer):

    groups = GroupSerializer(required=False, many=True)

    photo = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='image_size')

    groups_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, many=True, allow_null=True, queryset=Group.objects.all())

    class Meta:
        model = User
        exclude = (
            'password',
        )
    
    def update(self, instance, validated_data):
        groups_id = validated_data.pop('groups_id', None)
        if groups_id is not None:
            for group in list(instance.groups.all()):
                instance.groups.remove(group)
                    
            for id in groups_id:
                instance.groups.add(id)

        return super().update(instance, validated_data)

class VisitSerializer(serializers.Serializer):

    cagetory = serializers.CharField(max_length=16)
    
    cagetory__count = serializers.IntegerField()

class ContractSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()

    contractID = serializers.SerializerMethodField()

    validity = serializers.SerializerMethodField()

    visits = serializers.SerializerMethodField()
    
    class Meta:
        model = Contract
        fields = '__all__'

    def get_contractID(self, obj):
        return '%d-%s-%d' % (obj.user_id, obj.expiry_date.strftime("%Y%m%d") , obj.id)

    def get_validity(self, obj):
        return timezone.now().strftime('%Y-%m-%d') >= obj.issue_date.strftime('%Y-%m-%d') and timezone.now().strftime('%Y-%m-%d') <= obj.expiry_date.strftime('%Y-%m-%d')

    def get_visits(self, obj):
        order_list = Order.objects.filter(contract=obj).values('cagetory').annotate(count=Count('cagetory'))
        for i in order_list:
            print(i, '-------')
        print(order_list, 'end ===')
        return 'abc'

class AddressSerializer(serializers.ModelSerializer):
    
    user_id = serializers.IntegerField()

    title = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = '__all__'

    def get_title(self, obj):
        if obj.onMap:
            return obj.address

        return '%s / %s / %s / %s / %s' % (obj.city, obj.community, obj.street, obj.building, obj.roomNo)

    def update(self, instance, validated_data):
        defAddr = validated_data.get('defAddr', None)

        if defAddr:
            qs = Address.objects.filter(user_id=instance.user_id)
            for addr in qs:
                addr.defAddr = False
                addr.save()

        return super().update(instance, validated_data)

class SkillSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()

    class Meta:
        model = Skill
        fields = '__all__'

class WorkTimeSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()

    class Meta:
        model = WorkTime
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='image_size')
    
    user_id = serializers.IntegerField()
    
    class Meta:
        model = Resource
        fields = '__all__'