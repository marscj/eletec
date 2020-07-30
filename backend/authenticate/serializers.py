from django.contrib.auth import authenticate

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import AuthUser, PhoneConfirmation, EmailAddress, EmailConfirmationHMAC

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
            raise serializers.ValidationError("Please enter the correct phone number and otp for a account. Note that both fields may be case-sensitive.")
            
        validate_data['user'] = user
        return validate_data

class EmailKeySerliazer(serializers.Serializer):
    key = serializers.CharField(max_length=64)

class EmailAddressSerializer(serializers.Serializer):

    email = serializers.EmailField()

    verified = serializers.BooleanField(default=False)

class EmailCodeSerliazer(serializers.Serializer):

    email = serializers.EmailField()

    code = serializers.CharField(max_length=4)

    def validate(self, validate_data):
        email = validate_data.get("email")
        code = validate_data.get("code")

        try:
            email_address = EmailAddress.objects.get(email=email, code=code)
            email_address.verified = True
            email_address.save()
        except EmailAddress.DoesNotExist:
            raise serializers.ValidationError("Please enter the correct code")

        return validate_data