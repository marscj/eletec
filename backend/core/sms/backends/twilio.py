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
                    msg = requests.post(TWILIO_URL, data={
                        'Body': message.body,
                        'From': message.from_phone,
                        'To': '+971557199186'
                    }, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))

                    msg.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    if not self.fail_silently:
                        raise 