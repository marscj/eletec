from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import throttling
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ValidationError

import logging

from .models import PhoneConfirmation, EmailAddress, EmailConfirmationHMAC
from .serializers import PhoneSerializer, PhoneValidateSerializer, EmailAddressSerializer, EmailKeySerliazer

logger = logging.getLogger(__name__)

class GeneratePhone(APIView):
    queryset = PhoneConfirmation.objects.all()
    serializer_class = PhoneSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            try:
                PhoneConfirmation.create_otp_for_number(request, serializer.validated_data.get('phone_number'))
                return Response(serializer.data)
            except Exception as e:
                logger.error(e)
                return Response('Failed to send', status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidatePhone(APIView):
    queryset = PhoneConfirmation.objects.all()
    serializer_class = PhoneValidateSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            last_login = user.last_login
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)

            user_json = {
                "id": user.pk,
                "last_login": last_login,
                "token": token.key,
            }

            return Response(user_json)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenerateEmail(APIView):
    serializer_class = EmailAddressSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            try:
                EmailAddress.send_confirmation(request, serializer.validated_data.get('email'))
                return Response(serializer.data)
            except BaseException as e:
                logger.error(e)
                return Response('Failed to send', status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidateEmail(APIView):
    serializer_class = EmailKeySerliazer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            self.object = confirmation = self.get_object(serializer.validated_data.get('key'))
            confirmation.confirm(self.request)
            return Response('Verification succeeded!')
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, key):
        emailconfirmation = EmailConfirmationHMAC.from_key(key)
        
        if not emailconfirmation:
            raise ValidationError
        
        return emailconfirmation