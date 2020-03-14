from django.contrib.auth import authenticate

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import AuthUser, PhoneConfirmation

class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        exclude = (
            'password',
        )

class PhoneSerializer(serializers.Serializer):

    phone_number = PhoneNumberField(required=True)
    
class PhoneValidateSerializer(serializers.Serializer):
    
    phone_number = PhoneNumberField(required=True)
    
    otp = serializers.CharField(required=True, max_length=4)
    
    def validate(self, validate_data):
        phone_number = validate_data.get("phone_number")
        otp = validate_data.get("otp")

        user = authenticate(self.context['request'], phone_number=phone_number, otp=otp)

        if not user:
            raise serializers.ValidationError("Please enter the correct phone number and code for a account. Note that both fields may be case-sensitive.")
            
        validate_data['user'] = user

        return validate_data
