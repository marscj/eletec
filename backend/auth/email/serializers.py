from rest_framework import serializers

from .models import EmailAddress
from middleware.user import CurrentUserDefault

class EmailAddressSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    user_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))

    class Meta:
        model = EmailAddress
        fields = '__all__'

class EmailAddressValidateSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    otp = serializers.CharField(required=True, max_length=6)

    class Meta:
        model = EmailAddress
        fields = '__all__'

    def validate(self, validate_data):
        email = validate_data.get("email")
        otp = validate_data.get("otp")
        
        try:
            EmailAddress.objects.get(email=email, otp=otp)    
        except EmailAddress.DoesNotExist:
            raise serializers.ValidationError({'otp': 'Verification code error'})
            
        return validate_data