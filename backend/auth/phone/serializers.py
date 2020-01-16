from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login

from rest_framework import  serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import PhoneToken

User = get_user_model()

class PhoneTokenCreateSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(required=True)

    class Meta:
        model = PhoneToken
        fields = (
            'phone_number',
        )

class PhoneTokenUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class PhoneTokenValidateSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(required=True)
    otp = serializers.CharField(required=True, max_length=4)

    class Meta:
        model = PhoneToken
        fields = '__all__'
    
    def validate(self, validate_data):
        phone_number = validate_data.get("phone_number")
        otp = validate_data.get("otp")
        
        try:
            PhoneToken.objects.get(phone_number=phone_number, otp=otp)    
        except PhoneToken.DoesNotExist:
            raise serializers.ValidationError({'otp': 'Verification code error'})
            
        return validate_data
