from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

from rest_framework import  serializers

from .models import User, Address, Skill, WorkTime, Contract

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

class AddressSerializer(serializers.ModelSerializer):
    
    user_id = serializers.IntegerField()

    title = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = '__all__'

    def get_title(self, obj):
        if obj.onMap:
            return obj.address

        if obj.model == Address.Model.Personal:
            return '%s / %s / %s / %s / %s' % (obj.city, obj.community, obj.street, obj.building, obj.roomNo)
        else:
            return '%s / %s / %s / %s / %s' % (obj.city, obj.community, obj.street, obj.building, obj.officeNo)

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


class ContractSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()
    
    class Meta:
        model = Contract
        fields = '__all__'