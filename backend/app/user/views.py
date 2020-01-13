from rest_framework.response import Response
from rest_framework import views
from rest_framework import generics
from rest_framework import throttling

from django.conf import settings
from django.utils.crypto import get_random_string

import requests
import json

from .models import VerifyCode
from .serializers import PhoneNumberSerializer

class sendSms(views.APIView):
    throttle_classes = [throttling.UserRateThrottle]
    
    def post(self, request, *args, **kwargs):
        serializers = PhoneNumberSerializer(data=request.data)

        if serializers.is_valid(raise_exception=True):

            url = "https://api.twilio.com/2010-04-01/Accounts/%s/Messages.json" % settings.TWILIO_ACCOUNT_SID

            phone_number = serializers.data['phone_number']
            verify_code = get_random_string(4, '0123456789')

            response = requests.post(url, data={
                'Body': '[Eletec] Your verification code is %s' % verify_code,
                'From': settings.TWILIO_FROM_NUMBER,
                'To': phone_number
            }, auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))
                
            if response.ok:
                try: 
                    verify = VerifyCode.objects.get(phone_number=phone_number)
                    verify.verify_code = verify_code
                    verify.save()
                except VerifyCode.DoesNotExist:
                    verify = VerifyCode.objects.create(phone_number=phone_number, verify_code=verify_code)

                return Response(response.json(), status=response.status_code)
            else:
                return Response({'non_field_errors': [response.json().get('message', 'unknow error')]}, status=400)

            
