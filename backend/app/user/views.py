from rest_framework.response import Response
from rest_framework import views
from rest_framework import generics
from rest_framework import throttling

from django.conf import settings
from django.utils.crypto import get_random_string

import requests
import json

from .serializers import PhoneNumberSerializer

class sendSms(views.APIView):
    throttle_classes = [throttling.UserRateThrottle]
    
    def post(self, request, *args, **kwargs):
        serializers = PhoneNumberSerializer(data=request.data)

        if serializers.is_valid(raise_exception=True):

            url = "https://api.twilio.com/2010-04-01/Accounts/%s/Messages.json" % settings.TWILIO_ACCOUNT_SID

            phone_number = serializers.data['phone_number']

            print(phone_number)

            if settings.DEBUG:
                response = requests.post(url, data={
                    'Body':'[Eletec] Your verification code is %s' % get_random_string(4, '0123456789'),
                    'From':'+15005550006', 
                    'To':phone_number
                }, auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))
            else :
                response = requests.post(url, data={
                    'Body':'[Eletec] Your verification code is %s' % get_random_string(4, '0123456789'),
                    'From':'+13473086886',
                    'To': phone_number
                }, auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))

            if response.ok:
                print('ok')

            return Response(response.json(), status=response.status_code)
