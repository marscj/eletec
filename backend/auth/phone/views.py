from rest_framework.response import Response
from rest_framework import views, generics
from rest_framework import throttling

from django.conf import settings
from django.utils.crypto import get_random_string

import requests
import json

from .models import PhoneToken
from .serializers import PhoneTokenCreateSerializer, PhoneTokenValidateSerializer

from .utils import user_detail

# class sendSms(views.APIView):
#     throttle_classes = [throttling.UserRateThrottle]
    
#     def post(self, request, *args, **kwargs):
#         serializers = PhoneNumberSerializer(data=request.data, context={'request': request})

#         if serializers.is_valid(raise_exception=True):

#             phone_number = serializers.data['phone_number']
#             verify_code = get_random_string(4, '0123456789')

#             response = requests.post(settings.TWILIO_URL, data={
#                 'Body': '[Eletec] Your verification code is %s' % verify_code,
#                 'From': settings.TWILIO_FROM_NUMBER,
#                 'To': phone_number
#             }, auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))
                
#             if response.ok:
#                 try: 
#                     verify = VerifyCode.objects.get(phone_number=phone_number)
#                     verify.verify_code = verify_code
#                     verify.save()
#                 except VerifyCode.DoesNotExist:
#                     verify = VerifyCode.objects.create(phone_number=phone_number, verify_code=verify_code)

#                 return Response(response.json(), status=response.status_code)
#             else:
#                 print(response.json())
#                 return Response({'non_field_errors': [response.json().get('message', 'unknow error')]}, status=400)

class GenerateOTP(generics.CreateAPIView):
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenCreateSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def post(self, request, format=None):
        ser = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        if ser.is_valid():
            token = PhoneToken.create_otp_for_number(
                request.data.get('phone_number')
            )
            if token:
                phone_token = self.serializer_class(
                    token, context={'request': request}
                )
                data = phone_token.data
                if getattr(settings, 'PHONE_LOGIN_DEBUG', False):
                    data['debug'] = token.otp
                return Response(data)
            return Response({
                'reason': "you can not have more than {n} attempts per day, please try again tomorrow".format(
                    n=getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 10))}, status=status.HTTP_403_FORBIDDEN)
        return Response(
            {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)


class ValidateOTP(generics.CreateAPIView):
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenValidateSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def post(self, request, format=None):
        # Get the patient if present or result None.
        ser = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if ser.is_valid():
            pk = request.data.get("pk")
            otp = request.data.get("otp")
            try:
                user = authenticate(request, pk=pk, otp=otp)
                if user:
                    last_login = user.last_login
                login(request, user)
                response = user_detail(user, last_login)
                return Response(response, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(
                    {'reason': "OTP doesn't exist"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        return Response(
            {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)