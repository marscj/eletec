from rest_framework import serializers

from .models import EmailToken

class EmailTokenSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = EmailToken
        fields = '__all__'

class EmailTokenValidateSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    otp = serializers.CharField(required=True, max_length=6)

    class Meta:
        model = PhoneToken
        fields = '__all__'

    def validate(self, validate_data):
        email = validate_data.get("email")
        otp = validate_data.get("otp")
        
        try:
            EmailToken.objects.get(email=email, otp=otp)    
        except EmailToken.DoesNotExist:
            raise serializers.ValidationError({'otp': 'Verification code error'})
            
        return validate_data