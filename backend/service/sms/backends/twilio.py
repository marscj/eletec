from django.conf import settings

from .base import BaseSmsBackend

import requests
import json

TWILIO_URL = getattr(settings, "TWILIO_URL", "")
TWILIO_ACCOUNT_SID = getattr(settings, "TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = getattr(settings, "TWILIO_AUTH_TOKEN", "")
SENDSMS_FROM_NUMBER = getattr(settings, "SENDSMS_FROM_NUMBER", "")

class SmsBackend(BaseSmsBackend):
    def send_messages(self, messages):
        for message in messages:
            for to in message.to:
                try:
                    requests.post(settings.TWILIO_URL, data={
                        'Body': message.body,
                        'From': to,
                        'To': message.from_phone
                    }, auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN))
                except:
                    if not self.fail_silently:
                        raise
