from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import throttling
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .models import PhoneConfirmation, EmailAddress
from .serializers import PhoneSerializer, PhoneValidateSerializer, EmailSerializer

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
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            email_address, created = EmailAddress.objects.get_or_create(email=serializer.validated_data.get('email'), user=request.user)
            
            if created:
                email_address.send_confirmation(request)
            
            return Response(serializer.data)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)