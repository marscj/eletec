from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string
from django.conf import settings

from rest_framework.response import Response
from rest_framework import views, generics
from rest_framework import throttling
from rest_framework import status

from service.sms.message import SmsMessage

from .models import PhoneToken
from .serializers import PhoneTokenCreateSerializer, PhoneTokenValidateSerializer

from .utils import user_detail

class GenerateOTP(generics.CreateAPIView):
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenCreateSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def post(self, request, format=None):
        token = self.serializer_class(data=request.data, context={'request': request})
        
        if token.is_valid():
            otp = get_random_string(4, '0123456789')
            phone_number = token.data.get('phone_number')

            try: 
                phone_token = PhoneToken.objects.get(phone_number=phone_number)
                phone_token.otp = otp
                phone_token.save()
            except PhoneToken.DoesNotExist:
                PhoneToken.objects.create(phone_number=phone_number, otp=otp)

            from_phone = getattr(settings, 'SENDSMS_FROM_NUMBER')

            message = SmsMessage(
                body='[Eletec] Your verification code is %s' % otp,
                from_phone=from_phone,
                to=phone_number
            ).send()

            print(message)
            
            if message.ok:
                return Response(token.data)
            else:
                return Response({'error': 'failed to send'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(token.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidateOTP(generics.CreateAPIView):
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenValidateSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def post(self, request, format=None):
        ser = self.serializer_class(data=request.data, context={'request': request})
        if ser.is_valid():
            phone_number = request.data.get("phone_number")
            otp = request.data.get("otp")
            try:
                user = authenticate(request, phone_number=phone_number, otp=otp)
                if user:
                    last_login = user.last_login
                login(request, user)
                response = user_detail(user, last_login)
                return Response(response, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)