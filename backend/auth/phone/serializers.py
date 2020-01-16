from django.contrib.auth import get_user_model
from rest_framework import  serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import PhoneToken

User = get_user_model()

class PhoneTokenCreateSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(required=True)

    class Meta:
        model = PhoneToken
        fields = '__all__'


class PhoneTokenUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class PhoneTokenValidateSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(required=True)
    otp = serializers.CharField(max_length=4)

    class Meta:
        model = PhoneToken
        fields = '__all__'