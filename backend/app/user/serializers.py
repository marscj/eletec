from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

from rest_framework import  serializers

from .models import User, Address, Skill, WorkTime

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            'password',
        )

class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):

    content_type = ContentTypeSerializer(many=False)

    class Meta:
        model = Permission
        fields = '__all__'

class GroupDetailSerializer(serializers.ModelSerializer):
    
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

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'

class WorkTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkTime
        fields = '__all__'