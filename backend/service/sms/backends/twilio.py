import requests

from django.core.validators import ValidationError
from django.conf import settings

from .base import BaseSmsBackend
 
TWILIO_URL = getattr(settings, "SENDSMS_URL", "")
TWILIO_ACCOUNT_SID = getattr(settings, "SENDSMS_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = getattr(settings, "SENDSMS_AUTH_TOKEN", "")

class SmsBackend(BaseSmsBackend):
    def send_messages(self, messages):
        for message in messages:
            for to in message.to:
                try:
                    message = requests.post(TWILIO_URL, data={
                        'Body': message.body,
                        'From': message.from_phone,
                        'To': to
                    }, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))

                    if not message.ok:
                        print(message.json())
                        
                except Exception:
                    if not self.fail_silently:
                        raise
