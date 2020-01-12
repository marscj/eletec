from rest_framework.response import Response
from rest_framework import views
from rest_framework import generics
from rest_framework import throttling

from django.conf import settings
import requests
import json

class sendSms(views.APIView):
    throttle_classes = [throttling.UserRateThrottle]

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone_number', None)

        url = "https://api.twilio.com/2010-04-01/Accounts/%s/Messages.json" % settings.TWILIO_ACCOUNT_SID

        if settings.DEBUG:
            response = requests.post(url, data={
            'Body':'[Eletec] Your verification code is 0429',
            'From':'+15005550006',
            'To':'+9710557199186'
        }, auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))
        else :
            response = requests.post(url, data={
                'Body':'[Eletec] Your verification code is 0429',
                'From':'+13473086886',
                'To': phone
            }, auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))

        return Response(response.json(), status=response.status_code)
