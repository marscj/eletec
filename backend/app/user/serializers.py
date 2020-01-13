from rest_framework import  serializers

from phonenumber_field.phonenumber import to_python

from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class PhoneNumberField(serializers.CharField):
    default_error_messages = {"invalid": "Enter a valid phone number."}

    def to_internal_value(self, data):
        phone_number = to_python(data)
        if phone_number and not phone_number.is_valid():
            raise serializers.ValidationError(self.error_messages["invalid"])
        return phone_number

    def get_value(self, value):
        phone_number = value['phone_number']
        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number
        return phone_number

class PhoneNumberSerializer(serializers.Serializer):
    
    phone_number = PhoneNumberField(required=True)

