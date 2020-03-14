# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

# from .models import EmailAddress
# from middleware.user import CurrentUserDefault

# class EmailAddressSerializer(serializers.ModelSerializer):

#     email = serializers.EmailField()

#     user_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))

#     class Meta:
#         model = EmailAddress
#         fields = '__all__'

# class EmailAddressValidateSerializer(serializers.Serializer):

#     email = serializers.EmailField(required=True)

#     otp = serializers.CharField(required=True, max_length=6)

#     def validate(self, validate_data):
#         email = validate_data.get("email")
#         otp = validate_data.get("otp")
        
#         email_address = EmailAddress.objects.filter(email=email).last()

#         if email_address and email_address.otp != otp:
#             raise serializers.ValidationError({'otp': 'Verification code error'})
#         else:
#             raise serializers.ValidationError({'otp': 'Verification code error'})

#         email_address.verified = True
#         email_address.save()
        
#         # try:
#         #     email_address = EmailAddress.objects.get(email=email, otp=otp)
#         #     email_address.verified = True
#         #     email_address.save()
#         # except EmailAddress.DoesNotExist:
#         #     raise serializers.ValidationError({'otp': 'Verification code error'})
            
#         return validate_data