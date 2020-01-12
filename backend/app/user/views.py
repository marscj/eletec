from rest_framework.response import Response
from rest_framework import views
from rest_framework import generics
from rest_framework import throttling

from django.conf import settings
import requests
import json

if settings.DEBUG:
    account_sid = 'AC3d23045bf1213f916b7c082028412e53'
    auth_token = 'c54b1663080a2dae8eb0c7cf71bccdcf'
else:
    account_sid = 'ACcf794b0edd7c3f5a2d5be559eef0e254'
    auth_token = 'c3c8de0672d273e483e1e2f493c06da8'

class RandomRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1

class sendSms(views.APIView):
    throttle_classes = [throttling.UserRateThrottle]

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone_number', None)

        url = "https://api.twilio.com/2010-04-01/Accounts/%s/Messages.json" % account_sid

        if settings.DEBUG:
            response = requests.post(url, data={
            'Body':'[Eletec] Your verification code is 0429',
            'From':'+15005550006',
            'To':'+5571981265131'
        }, auth=(account_sid, auth_token))
        else :
            response = requests.post(url, data={
                'Body':'[Eletec] Your verification code is 0429',
                'From':'+13473086886',
                'To': phone
            }, auth=(account_sid, auth_token))

        print(response.json())

        return Response({'ok'})
