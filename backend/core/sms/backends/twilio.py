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
            try:
                return requests.post(TWILIO_URL, data={
                    'Body': message.body,
                    'From': message.from_phone,
                    'To': message.to
                }, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
                    
            except Exception:
                if not self.fail_silently:
                    raise
                
