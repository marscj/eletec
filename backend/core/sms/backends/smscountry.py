import requests

from django.core.validators import ValidationError
from django.conf import settings

from .base import BaseSmsBackend
 
URL = getattr(settings, "SENDSMS_URL", "")
USER = getattr(settings, "SENDSMS_USER", "")
PASSWORD = getattr(settings, "SENDSMS_PASSWORD", "")

class SmsBackend(BaseSmsBackend):
            
    def send_messages(self, messages):
        for message in messages:
            for to in message.to:
                try:
                    params = {
                        'user': USER,
                        'passwd': PASSWORD,
                        'mobilenumber' : to,
                        'message': message.body
                        'mtype':'N',
                        'DR':'Y'
                    }
                    msg = requests.get(URL, params)

                    msg.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    if not self.fail_silently:
                        raise 