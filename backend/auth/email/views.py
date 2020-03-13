from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string
from django.conf import settings

from smtplib import SMTPException

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import views, generics
from rest_framework import throttling
from rest_framework import status

from .models import EmailAddress
from .serializers import EmailAddressSerializer, EmailAddressValidateSerializer
from service.email.utils import render_mail

class GenerateOTP(generics.CreateAPIView):
    
    queryset = EmailAddress.objects.all()
    serializer_class = EmailAddressSerializer
    throttle_classes = [throttling.UserRateThrottle]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        token = self.serializer_class(data=request.data, context={'request': request})
        
        if token.is_valid():
            otp = get_random_string(4, '0123456789')
            email = token.data.get('email')
            from_phone = settings.DEFAULT_FROM_EMAIL

            try: 
                email_token = EmailAddress.objects.get(email=email)
                email_token.otp = otp
                email_token.save()
            except EmailAddress.DoesNotExist:
                EmailAddress.objects.create(email=email, otp=otp)

            message = render_mail(
                'verify_email.html',
                'Please Confirm Your E-mail Address',
                from_phone,
                email,
                {'otp': otp}
            )

            try:
                message.send()
                return Response(token.data)
            except SMTPException as e:
                return Response({'error': 'failed to send'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(token.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidateOTP(generics.CreateAPIView):

    queryset = EmailAddress.objects.all()
    serializer_class = EmailAddressValidateSerializer
    throttle_classes = [throttling.UserRateThrottle]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        
        token = self.serializer_class(data=request.data, context={'request': request})
        
        if token.is_valid():
            token.verified = True
            token.save()

            return(token.data)

        return Response(token.errors, status=status.HTTP_400_BAD_REQUEST)
